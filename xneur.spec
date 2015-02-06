%define name xneur
%define soname 17
%define libname %mklibname %{name} %{soname}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	0.17.0
Release:	2
URL:		http://www.xneur.ru
License:	GPLv2
Source0:	%{name}-%{version}.tar.gz
Patch0:		xneur-0.12.0-cflags.patch
Patch2:		xneur-0.16.0-link.patch
Group:		System/X11
Summary:	X Neural Switcher
BuildRequires:  pkgconfig(libpcre)
BuildRequires:	pkgconfig(enchant)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  aspell-devel
BuildRequires:  xosd-devel 
BuildRequires:	gettext-devel
Requires:	aspell-ru
Suggests:	gxneur

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout.

%package -n %{develname}
Summary:	Include Files and Libraries  
Group:		Development/X11
Requires:	%{libname} = %{version}  
Provides:	xneur-devel = %{version}  
Obsoletes:	xneur-devel < 0.11.1
Obsoletes:	xneur-%{_lib}xneur-devel < %{version}
  
%description -n %{develname} 
Development files for the package XNeur.

%package -n %{libname}
Summary:	XNeur Shared Library
Group:		System/Libraries
Obsoletes:	xneur-%{_lib}xneur11

%description -n %{libname}
Shared libraries for the package XNeur.

%prep
%setup -q
%patch0 -p0
%patch2 -p1

%build
autoreconf -fi
mv configure.in.orig configure.in
%configure2_5x
%make

%install
%makeinstall_std
%{__rm} -f %{buildroot}%{_libdir}/{%{name}/*.*a,*.*a}  
%find_lang %{name}  

%post
ln -s %{_datadir}/%name/languages/ru %{_datadir}/%name/languages/ru\(winkeys\)
  
%files -f %{name}.lang  
%doc AUTHORS ChangeLog NEWS README TODO  
%{_datadir}/%{name}  
%{_bindir}/*  
%dir %{_libdir}/%{name}  
%{_libdir}/%{name}/libxn*.so.*  
%doc %{_mandir}/man1/*  
%doc %{_mandir}/man5/*  
%dir %{_sysconfdir}/%{name}  
# Upstream updates a config file. So we must replace it.  
%config %{_sysconfdir}/%{name}/*
%{_datadir}/icons/* 
  
%files -n %{libname} 
%{_libdir}/libxn*.so.* 
  
%files -n %{develname}
%{_libdir}/*.so  
%dir %{_libdir}/%{name}  
%{_libdir}/%{name}/*.so  
%{_libdir}/pkgconfig/*.pc  
%{_includedir}/%{name}