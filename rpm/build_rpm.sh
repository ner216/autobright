#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
PROJECT_DIR=$(cd -- "$SCRIPT_DIR/.." && pwd)
SPEC_FILE="$SCRIPT_DIR/autobright.spec"
RPM_TOPDIR=${RPM_TOPDIR:-"$HOME/rpmbuild"}

if ! command -v rpmbuild >/dev/null 2>&1; then
	printf 'Error: rpmbuild is required (install the rpm-build package).\n' >&2
	exit 1
fi

VERSION=$(awk '$1 == "Version:" { print $2; exit }' "$SPEC_FILE")
if [[ -z "$VERSION" ]]; then
	printf 'Error: could not read Version from %s.\n' "$SPEC_FILE" >&2
	exit 1
fi

mkdir -p "$RPM_TOPDIR"/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
SOURCE_ARCHIVE="$RPM_TOPDIR/SOURCES/autobright-$VERSION.tar.gz"

tar -czf "$SOURCE_ARCHIVE" \
	--transform="s,^,autobright-$VERSION/," \
	-C "$PROJECT_DIR" \
	LICENSE README.md debian/autobright.service src/autobright

rpmbuild -bb --define "_topdir $RPM_TOPDIR" "$SPEC_FILE"

printf 'RPM built in %s/RPMS/noarch/\n' "$RPM_TOPDIR"


