Summary:	Control your GPG keys
Name:		kgpg
Version:	20.04.1
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		http://utils.kde.org/projects/kgpg
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(ECM)
BuildRequires:	gpgme-devel
BuildRequires:	boost-devel

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%files -f kgpg.lang
%{_datadir}/qlogging-categories5/kgpg.categories
%{_bindir}/*
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/kxmlgui5/kgpg
%{_datadir}/kgpg
%{_datadir}/kservices5/ServiceMenus/*.desktop
%{_sysconfdir}/xdg/autostart/org.kde.kgpg.desktop
%{_datadir}/applications/org.kde.kgpg.desktop
%{_datadir}/config.kcfg/kgpg.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kgpg --with-html
