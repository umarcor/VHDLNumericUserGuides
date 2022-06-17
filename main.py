#!/usr/bin/env python

from pathlib import Path
from shutil import which

from pyGHDL.dom.NonStandard import Design, Document


docs = Path(__file__).parent / "docs/ieee"
docs.mkdir(parents=True, exist_ok=True)

libraryPath = Path(which('ghdl')).parent.parent / 'lib/ghdl/src/ieee2008'
sourceFiles = sorted([source.stem for source in libraryPath.glob('*.vhdl')])

packages = []
contexts = []
otherFiles = []

for sourceFile in sourceFiles:
  print(sourceFile)
  if 'context' in sourceFile:
    contexts.append(sourceFile)
  elif 'body' not in sourceFile:
    body = f"{sourceFile}-body"
    if body in sourceFiles:
      packages.append(sourceFile)
    else:
      otherFiles.append(sourceFile)

print("· Contexts")
for item in contexts:
  print(" -", item)

print("· Packages")
for item in packages:
  print(" - ", item)

print("· Other")
for item in otherFiles:
  print(" - ", item)

# Numeric_bit and numeric_bit_unsigned
# std_logic_1164 and std_logic_textio
# Numeric_std and numeric_std_unsigned
# Math real and math complex
# Fixed-point and floating-point packages



# if source.stem not in [
#    'numeric_std',
#    'numeric_bit'
#]

#documents = []

#design = Design()
#library = design.GetLibrary("vhdl_ieee")
#for sourceFile in sourceFiles:
#    print(sourceFile)
#    document = Document(libraryPath / f"{sourceFile}.vhdl")
#    design.AddDocument(document, library)
#    documents.append(document)

#for document in documents:
#    for package in document.Packages:
#        if isinstance(package, PackageInstantiation):
          # Skip still not supported Generic Package Instances
#          continue
#        print(f"{package.Identifier}")
#        for item in package.DeclaredItems:
#            print(f"{item}")
