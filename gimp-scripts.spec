%define gimp_ver 26

Name:		gimp-scripts
Summary:	Collection of script-FUs for GIMP
Version:	38
Release:	1
License:	GPLv2+ and GPLv3+
Group:		Graphics
URL:		http://www.gimphelp.org
Source0:	http://www.gimphelp.org/DL/gimp_scripts_%{gimp_ver}.tar.bz2
BuildArch:	noarch
Requires:	gimp >= 2.6

%description
Script-FUs working with gimp 2.6.

%prep
%setup -q -n gimp_scripts_%{gimp_ver}

%build

%install
install -d %{buildroot}%{_datadir}/gimp/2.0/scripts/
install -m 644 *.scm %{buildroot}%{_datadir}/gimp/2.0/scripts/
cp -ar Presets %{buildroot}%{_datadir}/gimp/2.0/scripts/Presets

%files
%{_datadir}/gimp/2.0/scripts/*
%doc README.txt
