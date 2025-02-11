%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

%define oname	wmCalClock

Name: 	 	wmcalclock
Summary: 	Calendar and clock application for Window Maker
Version: 	1.25
Release: 	3
URL:		https://dockapps.windowmaker.org/file.php/id/9
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	http://dockapps.windowmaker.org/download.php/id/16/%{oname}-%{version}.tar.gz
Source2:	clock-icon.png

BuildRequires:	imagemagick
BuildRequires:	apmd-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

Conflicts:	WindowMaker < 0.95.0-3

%description
wmCalClock is a calendar and clock application for Window Maker.

%prep
%setup -qn %{oname}-%{version}

%build
export CC=gcc
export CXX=g++
pushd Src
%make_build CFLAGS="%{optflags}" CCOPTS="%{ldflags}"
popd
										
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
pushd Src
install -s -m 0755 wmCalClock %{buildroot}/%{_bindir}
install -m 0644 wmCalClock.1 %{buildroot}/%{_mandir}/man1/
popd

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=WMbattery
Comment=Calender & Clock docklet
Categories=System;
EOF

#icons
mkdir -p %{buildroot}/%{_liconsdir}
convert -size 48x48 %{SOURCE2} %{buildroot}/%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert -size 32x32 %{SOURCE2} %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert -size 16x16 %{SOURCE2} %{buildroot}/%{_miconsdir}/%{name}.png

%files
%doc TODO README
%{_bindir}/%{oname}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%doc %{_mandir}/*/*



%changelog
* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.25-1
+ Revision: 768143
- added missing BR
- imported package wmcalclock


* Wed Jul 08 2009 mdawkins <mattydaw@gmail.com> 1.25-1
- created separate pkg from WindowMaker
- updated url

