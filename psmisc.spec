Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	22.21
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://download.sourceforge.net/psmisc/%{name}-%{version}.tar.gz
# Source0-md5:	935c0fd6eb208288262b385fa656f1bf
Patch0:		%{name}-fuser.patch
URL:		http://psmisc.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser. The pstree command displays a tree
structure of all of the running processes on your system. The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name. The fuser command identifies the PIDs of
processes that are using specified files or filesystems.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__automake}
%{__autoheader}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT%{_sbindir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS Chang* NEWS README
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

