%define rel 1
%define name xneur
%define soname 12
%define libname %mklibname %{name} %{soname}
%define develname %mklibname %{name} -d

Name:		%{name}
Version:	0.12.0
Release:	%mkrel %{rel}
URL:		http://www.xneur.ru
License:	GPLv2
Source:		%{name}-%{version}.tar.bz2
Group:		System/X11
Summary:	X Neural Switcher
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{_lib}pcre-devel
BuildRequires:	enchant-devel
BuildRequires:  glib2-devel aspell-devel libgomp-devel
BuildRequires:  xosd-devel gstreamer0.10-devel libnotify-devel
Requires: aspell-ru
Recommends:	gxneur

%description
X Neural Switcher (http://www.xneur.ru).
Automatical switcher of keyboard layout.

%package -n %{develname}
Summary:        Include Files and Libraries  
Group:          Development/X11
Requires:       {_lib}xneur%{soname} = %{version}  
Requires:       %{name} = %{version}  
Requires:       pcre-devel
Provides:       xneur-devel = %{version}  
Obsoletes:      xneur-devel < 0.11.1  
  
%description -n %{develname} 
Development files for the package XNeur.

%package -n %{libname}
Summary:        XNeur Shared Library
Group:          System/Libraries
Provides:	libxnconfig%{soname} = %{version}
Obsoletes:	libxnconfig%{soname} < %{version}

%description -n %{libname}
Shared libraries for the package XNeur.

%prep
%setup -n %{name}-%{version} -q
#%patch0
# a hack for libaspell
%if %{_arch} == x86_64
sed -i -e "s/aspell_dir\/lib/aspell_dir\/lib64/" configure
%endif

%build
./configure --libdir=%{_libdir} --prefix=/usr
make %{?jobs:-j %jobs}

%install
%{makeinstall}  
# and some other hacks
#%if %{_arch} == x86_64
#mkdir $RPM_BUILD_ROOT/usr/lib64/
#mv -f $RPM_BUILD_ROOT/usr/lib/* $RPM_BUILD_ROOT/usr/lib64/
#%endif
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
