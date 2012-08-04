Name:		kgpg
Summary:	Control your GPG keys
Version: 4.9.0
Release: 1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kgpg
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files
%{_kde_appsdir}/kgpg
%{_kde_bindir}/kgpg
%{_kde_iconsdir}/*/*/apps/kgpg.*
%{_kde_applicationsdir}/kgpg.desktop
%{_kde_services}/ServiceMenus/encryptfile.desktop
%{_kde_services}/ServiceMenus/encryptfolder.desktop
%{_kde_services}/ServiceMenus/viewdecrypted.desktop
%{_kde_autostart}/kgpg.desktop
%{_kde_datadir}/config.kcfg/kgpg.kcfg
%{_kde_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_kde_docdir}/HTML/*/kgpg

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

