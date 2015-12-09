#!/usr/bin/env bash

#unzip the bitcode
gunzip -k yices_main.bc.gz
gunzip -k libpoly.so.bc.gz 

# Build the manifest file
cat > yices_smt2.manifest <<EOF
{ "modules" : ["yices_smt2.bc"]
, "binary"  : "yices_smt2"
, "libs"    : ["libpoly.so.bc"]
, "native_libs" : ["-lc", "-lgmp"]
, "search"  : ["/usr/lib", "/usr/local/lib", "/usr/lib/x86_64-linux-gnu/"]
, "args"    : ["--mcsat"]
, "name"    : "yices_smt2"
}
EOF

# Previrtualize
${OCCAM_HOME}/bin/occam previrt --work-dir=previrt yices_smt2.manifest


