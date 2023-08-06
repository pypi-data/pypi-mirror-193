"""
The scoop template engine (ste) is meant to facilitate the preparation of LaTeX
documents to abide to the formatting standards for various scientific
journals. Please visit 
https://gitlab.com/scoopgroup-public/scoop-template-engine 
for a full description of the features.
"""

# Resolve the dependencies.
import argparse
import datetime
import glob
import importlib.metadata 
import importlib.resources
import importlib.util
import inspect
import itertools
import operator
import os
import packaging.version
import pathlib
import re
import shutil
import sys
import yaml
from subprocess import run, STDOUT
from multiprocessing import Pool, cpu_count

def removePrefix(text, prefix):
  """
  removes a prefix from a string when present.
  """
  if text.startswith(prefix):
    return text[len(prefix):]
  else:
    return text

def extractTemplateDescription(text, templateName):
  """
  extracts the template description present in the form
    <<TemplateDescription templateName: description>> or else
    <<TemplateDescription: description>>
  from the text.
  """
  # Try and find a template specific description first.
  templateDescription = re.findall('<<TemplateDescription ' + templateName + ':\s*(.*?)>>|$', text)[0]
  # If that did not turn up anything, try and find a generic template description.
  if not templateDescription:
    templateDescription = re.findall('<<TemplateDescription:\s*(.*?)>>|$', text)[0]
  return templateDescription

def extractDependencies(text, templateName):
  """
  extracts the dependencies present in the form
    <<Dependency templateName: file>> and
    <<Dependency: file>>                         
  from the text.
  """
  # Try and find template specific depencies first.
  dependencies = list(filter(None, re.findall('<<Dependency ' + templateName + ':\s*(.*?)>>|$', text)))
  # In addition, try and find generic depencies.
  dependencies = dependencies + list(filter(None, re.findall('<<Dependency:\s*(.*?)>>|$', text)))
  return dependencies

def extractVersionRequirement(text):
  """
  verifies whether the template's resources are compatible with the template.
  The template's minimum required version (if any) is specified in the form
  <<MinimumVersion: 1.2.3>>
  """
  # Try to find a minimum version requirement, if any.
  minimumVersion = re.search('<<MinimumVersion:\s*([0-9.]*)>>|$', text).group(1)
  return minimumVersion

def init(data, baseDirectory):
  """
  runs a script (typically init.py) and catches its stdout and stderr in a .log file.
  """
  # Construct the absolute path of the init.py file under consideration.
  folder = data[0]
  scriptname = data[1]
  scriptnameAbsolutePath = os.path.abspath(os.path.join(f'{folder}', f'{scriptname}'))
  scriptnameRelativePath = os.path.relpath(scriptnameAbsolutePath, start = baseDirectory)

  # Create the .log file with file name derived from the scriptname file name.
  logfilename = os.path.splitext(scriptnameAbsolutePath)[0] + '.log'
  print('Running {0:s}'.format(scriptnameRelativePath))
  with open(logfilename, 'w') as logfile:
    # Run the scriptname, capture its stdout and stderr and return value.
    returnValue = run([scriptnameAbsolutePath], cwd = folder, stdout = logfile, stderr = STDOUT)

  # Remember the script in case of failure.
  if returnValue.returncode != 0:
    return (False, folder, scriptname, logfilename)
  return (True, )

def main():
  """
  implements the user interface to the Scoop Template Engine.
  """

  # Remember who we are and how we were called.
  thisScriptName = os.path.basename(sys.argv[0])
  thisScriptAbsolutePath = os.path.abspath(sys.argv[0])
  thisScriptCallSummary = " ".join([thisScriptName] + sys.argv[1:])
  thisScriptAbsolutePathCallSummary = " ".join(sys.argv)
  baseDirectory = str(importlib.resources.files("ste"))
  
  # Get the version number.
  try:
    scoopTemplateEngineVersion = importlib.metadata.version("scoop-template-engine")
  except:
    scoopTemplateEngineVersion = "VERSION ERROR"

  # Specify some default values.
  dataFile = None
  outFileSuffix = True

  # Define some constants.
  templatePrefix = "template-"

  # Define the command line argument parser.
  parser = argparse.ArgumentParser(description = 'The scoop template engine (version {version:s}).'.format(version = scoopTemplateEngineVersion), formatter_class = argparse.RawTextHelpFormatter)
  parser.add_argument('--datafile', metavar = 'data.yaml', help = '.yaml file containing document data\n(default: the unique .yaml or .yml file in the current directory)', nargs = '?')
  parser.add_argument('--template', metavar = 'name of template', help = 'name of template to be used', nargs = '?')
  parser.add_argument('--prefix', metavar = 'output filename prefix', help = '<prefix>-<template>.tex file will be generated\n(default: derived from datafile)', nargs = '?', default = None)
  parser.add_argument('--outdir', metavar = 'output directory', help = 'generated files will be written to this directory\n(default: current directory)', nargs = '?', default = None)
  parser.add_argument('--nosuffix', help = 'generate <prefix>.tex rather than <prefix>-<template>.tex', action = 'store_true')
  parser.add_argument('--nocustombib', help = 'do not generate a custom .bib file', action = 'store_true')
  parser.add_argument('--nobib', help = 'do not use any .bib files', action = 'store_true')
  parser.add_argument('--quiet', help = 'do not report anything\n\n', action = 'store_true')
  parser.add_argument('--listtemplates', metavar = 'directories', help = 'list available templates in the directories (recursively) and exit', nargs = '*', default = None)
  parser.add_argument('--init', help = 'initialize all template resources and exit', action = 'store_true')
  parser.add_argument('--version', help = 'write out the version number and exit', action = 'store_true')
  args = parser.parse_args()

  # Define a print function which honors the --quiet option.
  quietprint = print if not args.quiet else lambda *args, **kwargs: None

  # If --version is given, report the version number and exit.
  if args.version:
    print(scoopTemplateEngineVersion)
    sys.exit(0)


  # If --init is given, run all manuscripts/**/init.py scripts and exit.
  if args.init:
    print('Initializing the template resources...')
    # Collect the init.py files to be executed, and the relative names of the
    # folders they are in.
    baseFolder = os.path.join(baseDirectory, 'manuscripts')
    fileList = []
    for filename in glob.glob(f'{baseFolder}/**/init.py', recursive = True):
      scriptname = os.path.basename(filename)
      folder = os.path.dirname(filename)
      fileList.append((folder, scriptname))

    # Get the number of CPUs for parallel processing.
    nCPU = cpu_count()

    # Execute all scripts in parallel (by calling the init function) and catch
    # their return values.
    with Pool(nCPU) as p:
      returnValues = p.starmap(init, zip(fileList, itertools.cycle([baseDirectory])))

      # Filter the return values for failed scripts.
      failedList = [(x[1], x[2], x[3]) for x in returnValues if not x[0]]

      # Try the scripts which failed again.
      returnValues = p.map(init, failedList)

      # Filter the return values for failed scripts.
      failedList = [(x[1], x[2], x[3]) for x in returnValues if not x[0]]

      # Show the scripts which failed twice.
      if len(failedList) > 0:
        print()
        print('The following scripts failed twice:')
        for item in failedList:
          print('{0:s}/{1:s}'.format(item[0], item[1]))
          print('See {0:s} for details.'.format(item[2]))
        print('Associated templates will not be available.')

    sys.exit(0)


  # If --listtemplates is given, list all templates and their descriptions and exit.
  if isinstance(args.listtemplates, list):
    templateFiles = []
    # Find all template files in any of the template directories specified (default: '.').
    if not args.listtemplates:
      args.listtemplates.append('.')
    for templateDirectory in args.listtemplates:
      templateFiles.extend(glob.glob(baseDirectory + '/**/' + templateDirectory + '/**/' + templatePrefix + '*.tex', recursive = True))

    # Canonicalize each template file's file name and strip the baseDirectory from its name.
    templateFiles = [os.path.abspath(templateFile) for templateFile in templateFiles]

    # Extract the template description from each template file.
    templateList = []
    for templateFile in templateFiles:
      # Determine whether the template file is a regular file or a link.
      templateFileIsLink = os.path.islink(templateFile)

      # Open the template file.
      try:
        with open(templateFile) as templateFileStream:
          templateFileData = templateFileStream.read()
      except IOError:
        print()
        print('ERROR: Template file {file:s} is not readable.'.format(file = templateFile))
        sys.exit(1)

      # Extract the template decription from the template.
      templateBaseName = re.findall('.*/' + templatePrefix + '(.*?)\.tex', templateFile)[0]
      templateDescription = extractTemplateDescription(templateFileData, templateBaseName)

      # Verify whether the template uses BibLaTeX.
      templateUsesBibLaTeX = '<<BibLaTeXResources>>' in templateFileData

      # Collect the information in the template list.
      templateList.append([templateBaseName, 
        templateUsesBibLaTeX, 
        templateDescription, 
        str(pathlib.Path(templateFile).relative_to(baseDirectory)), 
        templateFileIsLink])

    # Find the maximal lengths of the entries in each column of the template list.
    if not templateList:
      sys.exit(0)
    formatString = ""
    formatString = formatString + "{template:" + str(max([len(item[0]) for item in templateList])) + "s}"
    formatString = formatString + "  {BibLaTeX:" + "1s}"
    formatString = formatString + "  {isLink:" + "1s}"
    formatString = formatString + "  {description:" + str(max([len(item[2]) for item in templateList])) + "s}"
    formatString = formatString + "  {file:" + str(max([len(item[3]) for item in templateList])) + "s}"

    # Print the list of template information, sorted by template description with duplicates removed.
    templateList = [list(template) for template in set(tuple(template) for template in templateList)]
    templateList.sort(key = operator.itemgetter(1))
    for template in templateList:
      print(formatString.format(template = template[0], BibLaTeX = '*' if template[1] else '-', isLink = 'L' if template[4]  else 'F', description = template[2], file = template[3])) 
    sys.exit(0)

  # Print a greeting.
  quietprint('The scoop template engine (version {version:s}).'.format(version = scoopTemplateEngineVersion))

  # Get and process the --dataFile argument from the parser.
  dataFile = args.datafile
  if not dataFile:
    # Try to locate the unique .yaml or .yml file in the current directory. 
    dataFile = glob.glob('*.yaml') + glob.glob('*.yml')
    if len(dataFile) == 0:
      print("No .yaml or .yml file found was found in the current directory.")
      print("Please specify the YAML document data file to use via --datafile.")
      print("No output was produced.")
      sys.exit(1)
    if len(dataFile) != 1:
      print("More than one .yaml or .yml file was found in the current directory.")
      print("Please specify the YAML document data file to use via --datafile.")
      quietprint("The following .yaml or .yml files were found:")
      quietprint('\n'.join(dataFile))
      print("No output was produced.")
      sys.exit(1)
    dataFile = dataFile[0]

  # Get and process the --template argument from the parser.
  templateBaseName = args.template

  # Get and process the --prefix argument from the parser.
  outFileBaseName = args.prefix

  # Get and process the --outdir argument from the parser.
  outDirectory = args.outdir

  # Get and process the --nocustombib argument from the parser.
  customBib = not args.nocustombib

  # Get and process the --nobib argument from the parser.
  noBib = args.nobib

  # Report the data file to the user. 
  quietprint("\nscoop template engine version {version:s}".format(version = scoopTemplateEngineVersion))
  quietprint("Using datafile:       {file:s}".format(file = dataFile))

  # Read the .yaml dataFile.
  try:
    with open(dataFile) as dataFileStream:
      dataFileData = yaml.safe_load(dataFileStream)
      if not dataFileData:
        dataFileData = {}
  except IOError:
    print()
    print("ERROR: dataFile {file:s} is not readable.".format(file = dataFile))
    print("No output was produced.")
    sys.exit(1)

  # Process and remove the "outdir" key from the dataFile, unless we already have it from the command line.
  if not outDirectory:
    outDirectory = dataFileData.get("control", {}).get("outdir")
  dataFileData.pop("outdir", None)
  if not outDirectory:
    outDirectory = "./"

  # Process and remove the "prefix" key from the dataFile, unless we alredy have it from the command line.
  if not outFileBaseName:
    outFileBaseName = dataFileData.get("control", {}).get("prefix")
  if not outFileBaseName:
    outFileBaseName = os.path.splitext(dataFile)[0]
  dataFileData.pop("prefix", None)

  # Process and remove the "nocustombib" key from the dataFile, unless we alredy have it from the command line.
  if customBib:
    if dataFileData.get("control", {}).get("nocustombib"):
      customBib = False
  dataFileData.pop("nocustombib", None)

  # Process and remove the "nobib" key from the dataFile, unless we alredy have it from the command line.
  if not noBib:
    if dataFileData.get("control", {}).get("nobib"):
      noBib = True
  dataFileData.pop("nobib", None)

  # Process and remove the "template" key from the dataFile, unless we already have it from the command line.
  if not templateBaseName:
    templateBaseName = dataFileData.get("control", {}).get("template")
  dataFileData.pop("template", None)

  # Make sure we have a template file.
  if not templateBaseName:
    print("You need to specify a template file via --template or via the template key in the document data file.")
    print("No output was produced.")
    sys.exit(1)

  # Assemble the full name of the template file.
  templateFile = templatePrefix + templateBaseName 

  # Try to locate the unique .tex template file to be used.
  templateFile = glob.glob(baseDirectory + '/**/' + templateFile + '.tex', recursive = True)
  if len(templateFile) == 0:
    print("No template file matching '{templateBaseName:s}' was found in the current directory.".format(templateBaseName = templateBaseName))
    print("Please specify the template via --template.")
    print("No output was produced.")
    sys.exit(1)
  if len(templateFile) != 1:
    print("More than one .tex file is matching the pattern.")
    print("Please specify the template via --template unambiguously.")
    print("No output was produced.")
    quietprint("The following .yaml or .yml files were found:")
    quietprint('\n'.join(templateFile))
    sys.exit(1)
  templateFile = templateFile[0]
  templateFileExtension = os.path.splitext(templateFile)[1]
  templateDirectory = os.path.dirname(templateFile)

  # Infer the top-level component (such as 'manuscripts') of the directory the template resides in.
  templateTopLevelDirectory = pathlib.Path(templateFile).relative_to(baseDirectory).parts[0]

  # Report the template file to the user. 
  quietprint("Using templatefile:   {file:s}".format(file = os.path.relpath(templateFile, start = baseDirectory)))

  # Infer the rulesFile from the templateFile.
  rulesFile = os.path.join(baseDirectory, templateTopLevelDirectory, templateTopLevelDirectory + '.py')

  # Report the rules file to the user. 
  quietprint("Using rulesfile:      {file:s}".format(file = os.path.relpath(rulesFile, start = baseDirectory)))

  # Process the --nosuffix argument from the parser.
  if args.nosuffix:
    outFileSuffix = False

  # Process and remove the "nosuffix" key from the dataFile.
  if dataFileData.get("control", {}).get("nosuffix"):
    outFileSuffix = False
  dataFileData.pop("nosuffix", None)

  # Assemble the output file name.
  if outFileSuffix:
    outFileBaseName = outFileBaseName + '-' + templateBaseName + templateFileExtension
  else:
    outFileBaseName = outFileBaseName + templateFileExtension
  outFile = os.path.join(outDirectory, outFileBaseName)

  # Report the output file to the user. 
  quietprint("Writing to outFile:   {file:s}".format(file = outFile))

  # Read the template file.
  try:
    with open(templateFile) as templateFileStream:
      templateFileData = templateFileStream.read()
  except IOError:
    print()
    print('ERROR: Template file {file:s} is not readable.'.format(file = templateFile))
    print("No output was produced.")
    sys.exit(1)

  # Verify that the template's resources were initialized with a compatible
  # version of the template engine.
  # Extract the template's minimum version requirement (if any).
  minimumVersion = extractVersionRequirement(templateFileData)
  if minimumVersion:
    minimumVersion = packaging.version.Version(minimumVersion)
    # Get the version used to initialize the template's resources.
    stampFile = templateDirectory + '/SCOOP-STAMP'
    try:
      with open(stampFile) as stampFileStream:
        stampFileData = stampFileStream.read()
    except:
      print()
      print('ERROR: The resources for template {template:s} have not been initialized.'.format(template = templateBaseName))
      print('Please run')
      print('  {scriptName:s} --init'.format(scriptName = thisScriptName))
      sys.exit(1)
    versionInitialized = packaging.version.Version(stampFileData.split('\n')[0])
    # Verify whether the version requirement is met.
    if versionInitialized < minimumVersion:
      print()
      print('ERROR: The resources for template {template:s} are outdated.'.format(template = templateBaseName))
      print('Please run')
      print('  {scriptName:s} --init'.format(scriptName = thisScriptName))
      sys.exit(1)

  # Remove all version tags from the template.
  templateFileData = re.sub(r'<<MinimumVersion.*>>.*\n', '', templateFileData)

  # Find the dependencies in the template.
  dependencies = extractDependencies(templateFileData, templateBaseName)

  # Copy all dependencies of the template to the outDirectory.
  for dependency in dependencies:
    sourceFile = templateDirectory + "/" + dependency
    sourceFileRelativePath = os.path.relpath(sourceFile, start = baseDirectory)
    destinationFile = outDirectory + "/" + dependency
    quietprint("Copying               {sourceFile:s} to {outDirectory:s}".format(sourceFile = sourceFileRelativePath, outDirectory = outDirectory))
    os.makedirs(os.path.dirname(destinationFile), exist_ok = True)
    shutil.copy(sourceFile, destinationFile, follow_symlinks = True)

  # Remove all dependency tags from the template.
  templateFileData = re.sub(r'<<Dependency.*>>.*\n', '', templateFileData)

  # Find the switches for the creation of a custom bibliography in the template.
  customBibliographySwitches = " ".join(re.findall('<<CreateCustomBibliography:\s*(.*?)>>', templateFileData))

  # Remove all switches for the creation of a custom bibliography from the template.
  templateFileData = re.sub(r'<<CreateCustomBibliography.*>>.*\n', '', templateFileData)

  # Find the template description in the template.
  templateDescription = extractTemplateDescription(templateFileData, templateBaseName)

  # Remove all template description tags from the template.
  templateFileData = re.sub(r'<<TemplateDescription.*>>.*\n', '', templateFileData)

  # Report the template description to the user. 
  quietprint("Template description: {description:s}".format(description = templateDescription))

  # Import the rules file, which is supposed to provide functions to fill in the placeholders present in the template.
  spec = importlib.util.spec_from_file_location("scoop template engine rules", rulesFile)
  rules = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(rules)

  # Create an instance of a parserObject.
  from collections import namedtuple
  parserInfoStructure = namedtuple('parserInfo', ['dataFileData', 'outDirectory', 'outFileBaseName', 'templateBaseName', 'templateDescription', 'scoopTemplateEngineVersion', 'thisScriptAbsolutePathCallSummary', 'customBibliographySwitches', 'customBib', 'noBib'])
  parserInfo = parserInfoStructure(
      dataFileData = dataFileData, 
      outDirectory = outDirectory, 
      outFileBaseName = outFileBaseName, 
      templateBaseName = templateBaseName, 
      templateDescription = templateDescription, 
      scoopTemplateEngineVersion = scoopTemplateEngineVersion, 
      thisScriptAbsolutePathCallSummary = thisScriptAbsolutePathCallSummary, 
      customBibliographySwitches = customBibliographySwitches, 
      customBib = customBib, 
      noBib = noBib)
  parserFunctions = rules.parserObject(parserInfo)

  # Create a dictionary of substitutions to be performed on the template, recognized by the pattern '<<...>>'.
  substitutions = re.findall('<<(.*?)>>', templateFileData)
  substitutions = dict(zip(substitutions, [getattr(parserFunctions, substitution)() for substitution in substitutions]))

  # Apply the substitutions to the template.
  templateSpecialized = templateFileData
  for (replaceSource, replaceTarget) in substitutions.items():
    if replaceTarget is not None:
      templateSpecialized = templateSpecialized.replace("<<" + replaceSource + ">>", replaceTarget)

  # Prepend generation info including a time stamp.
  stampString = """% Generated by {scriptName:s} (version {version:s})
% on {dateTime:s} using
% {callSummary:s}

""".format(scriptName = thisScriptName, 
    version = scoopTemplateEngineVersion, 
    dateTime = datetime.datetime.utcnow().strftime("%Y%m%d-%H:%M:%S UTC"), 
    callSummary = thisScriptCallSummary)
  templateSpecialized = stampString + templateSpecialized

  # Write the outFile.
  try:
    with open(outFile, "w") as outFileStream:
      outFileData = outFileStream.write(templateSpecialized)
  except IOError:
    print()
    print('ERROR: outFile file {file:s} is not writable.'.format(file = outFile))
    sys.exit(1)



if __name__ == "__main__":
    sys.exit(main())
