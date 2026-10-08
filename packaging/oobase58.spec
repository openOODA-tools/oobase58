Name:           oobase58
Version:        0.2.0
Release:        1%{?dist}
Summary:        Cryptographic Base58 encoder and decoder omitting ambiguous alphanumeric glyphs.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oobase58
Source0:        oobase58-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oobase58 is a sovereign, capability-bounded BASE58 ENCODER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oobase58
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oobase58-uninstall

%files
/usr/bin/oobase58
/usr/bin/oobase58-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevated to v0.2.0 with pure native openOODA, multi-alphabet support, and MCP server
