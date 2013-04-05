Name:		kgpg
Summary:	Control your GPG keys
Version:	4.10.2
Release:	1
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

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.9.0-1
- New version 4.9.0

* Fri Jul 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.97-1
- New version 4.8.97

* Thu Jul 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.4-1
- update to 4.8.4

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.3-1
- update to 4.8.3

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.2-1
- update to 4.8.2

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 4.8.1-1
- update to 4.8.1

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.97-1
+ Revision: 758057
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.95-1
+ Revision: 744538
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.90-1
+ Revision: 739295
- New upstream tarball $NEW_VERSION

* Thu Nov 24 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.7.80-1
+ Revision: 733063
- Import kgpg
- Create folder

