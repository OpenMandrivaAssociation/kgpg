Name:    kgpg
Summary: Control your GPG keys
Version: 4.8.97
Release: 1
Group: Graphical desktop/KDE
License: LGPLv2
URL:     http://utils.kde.org/projects/%name
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/%{name}-%version.tar.xz

BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: kdepimlibs4-devel

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files
%_kde_appsdir/kgpg
%_kde_bindir/kgpg
%_kde_iconsdir/*/*/apps/kgpg.*
%_kde_datadir/applications/kde4/kgpg.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfile.desktop
%_kde_datadir/kde4/services/ServiceMenus/encryptfolder.desktop
%_kde_datadir/kde4/services/ServiceMenus/viewdecrypted.desktop
%_kde_datadir/autostart/kgpg.desktop
%_kde_datadir/config.kcfg/kgpg.kcfg
%_kde_datadir/dbus-1/interfaces/org.kde.kgpg.Key.xml
%_kde_docdir/HTML/*/kgpg

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
	
%make

%install
%makeinstall_std -C build

