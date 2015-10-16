Summary:	Control your GPG keys
Name:		kgpg
Version:	15.08.2
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/kgpg
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files
%{_kde_applicationsdir}/kgpg.desktop
%{_kde_appsdir}/kgpg
%{_kde_autostart}/kgpg.desktop
%{_kde_bindir}/kgpg
%{_kde_datadir}/config.kcfg/kgpg.kcfg
%{_kde_docdir}/HTML/*/kgpg
%{_kde_iconsdir}/*/*/apps/kgpg.*
%{_kde_services}/ServiceMenus/encryptfile.desktop
%{_kde_services}/ServiceMenus/encryptfolder.desktop
%{_kde_services}/ServiceMenus/viewdecrypted.desktop
%{_datadir}/appdata/kgpg.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
