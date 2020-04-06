%define _enable_debug_packages	%{nil}
%define debug_package		%{nil}

%define oname	wmCalClock
%define srcdirname    Src

Name: 	 	wmcalclock
Summary: 	Calendar and clock application for Window Maker
Version: 	1.25
Release: 	3
URL:		http://dockapps.windowmaker.org/file.php/id/9
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
%setup -q -n %{oname}-%{version}

%build
%make -C %{srcdirname} CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -D -m 755 %{srcdirname}/%{srcname} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{srcdirname}/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc BUGS CHANGES COPYING HINTS README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.25-1
+ Revision: 768143
- added missing BR
- imported package wmcalclock


* Wed Jul 08 2009 mdawkins <mattydaw@gmail.com> 1.25-1
- created separate pkg from WindowMaker
- updated url

