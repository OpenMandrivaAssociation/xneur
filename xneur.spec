%define rel 1
%define name xneur
%define soname 13
%define libname %mklibname %{name} %{soname}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	0.13.0
Release:	%mkrel %{rel}
URL:		http://www.xneur.ru
License:	GPLv2
Source:		%{name}-%{version}.tar.bz2
Patch0:		xneur-0.12.0-cflags.patch
#Patch1:		xneur-0.12.0-libnotify.patch
Patch2:		xneur-0.12.0-link.patch
Group:		System/X11
Summary:	X Neural Switcher
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pcre-devel
BuildRequires:	enchant-devel
BuildRequires:  glib2-devel aspell-devel
BuildRequires:  xosd-devel gstreamer0.10-devel libnotify-devel
BuildRequires:	gettext-devel
Requires:	aspell-ru
Suggests:	gxneur

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout.

%package -n %{develname}
Summary:        Include Files and Libraries  
Group:          Development/X11
Requires:       %{libname} = %{version}  
Provides:       xneur-devel = %{version}  
Obsoletes:      xneur-devel < 0.11.1
Obsoletes:	xneur-%{_lib}xneur-devel < %{version}
  
%description -n %{develname} 
Development files for the package XNeur.

%package -n %{libname}
Summary:        XNeur Shared Library
Group:          System/Libraries
Obsoletes:	xneur-%{_lib}xneur11

%description -n %{libname}
Shared libraries for the package XNeur.

%prep
%setup -n %{name}-%{version} -q
%patch0 -p0
#patch1 -p0
%patch2 -p0

%build
autoreconf -fi
%configure2_5x
%make

%install
rm -fr %buildroot
%{makeinstall_std}
%{__rm} -f %{buildroot}%{_libdir}/{%{name}/*.*a,*.*a}  
%find_lang %{name}  

%clean
rm -rf %{buildroot}

%post
ln -s %{_datadir}/%name/languages/ru %{_datadir}/%name/languages/ru\(winkeys\)
  
%files -f %{name}.lang  
%defattr(-,root,root)  
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
%defattr(-,root,root)  
%{_libdir}/libxn*.so.* 
  
%files -n %{develname}
%defattr(-,root,root)  
%{_libdir}/*.so  
%dir %{_libdir}/%{name}  
%{_libdir}/%{name}/*.so  
%{_libdir}/pkgconfig/*.pc  
%{_includedir}/%{name}
