%define gimp_ver 2.8

Name:		gimp-scripts
Summary:	Collection of script-FUs for GIMP
Version:	40
Release:	1
License:	GPLv2+ and GPLv3+
Group:		Graphics
URL:		http://www.gimphelp.org
Source0:	http://www.gimphelp.org/DL/gimp_scripts-%{gimp_ver}.tar.bz2
BuildArch:	noarch
Requires:	gimp >= %{gimp_ver}

%description
Script-FUs working with gimp 2.8.

%prep
%setup -q -n gimp_scripts-%{gimp_ver}

%build

%install
install -d %{buildroot}%{_datadir}/gimp/2.0/scripts/
install -d %{buildroot}%{_datadir}/gimp/2.0/gimpressionist/
install -m 644 *.scm %{buildroot}%{_datadir}/gimp/2.0/scripts/
cp -ar Presets %{buildroot}%{_datadir}/gimp/2.0/gimpressionist/Presets

%files
%{_datadir}/gimp/2.0/scripts/*
%{_datadir}/gimp/2.0/gimpressionist/Presets/*
