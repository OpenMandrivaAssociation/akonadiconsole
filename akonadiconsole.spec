Summary:	Console that helps to debug akonadi
Name:		akonadiconsole
Version:	16.12.1
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	ftp://ftp.kde.org/pub/kde/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	extra-cmake-modules
BuildRequires:	qgpgme-devel
BuildRequires:	sasl-devel
BuildRequires:	kf5akonadi-devel
BuildRequires:	kf5akonadicontact-devel
BuildRequires:	kf5akonadimime-devel
BuildRequires:	kf5calendarcore-devel
BuildRequires:	kf5calendarsupport-devel
BuildRequires:	kf5completion-devel
BuildRequires:	kf5config-devel
BuildRequires:	kf5configwidgets-devel
BuildRequires:	kf5contacts-devel
BuildRequires:	kf5crash-devel
BuildRequires:	kf5dbusaddons-devel
BuildRequires:	kf5doctools-devel
BuildRequires:	kf5i18n-devel
BuildRequires:	kf5itemmodels-devel
BuildRequires:	kf5libkdepim-devel
BuildRequires:	kf5libkleo-devel
BuildRequires:	kf5messageviewer-devel
BuildRequires:	kf5mime-devel
BuildRequires:	kf5pimtextedit-devel
BuildRequires:	kf5textwidgets-devel
BuildRequires:	kf5widgetsaddons-devel
BuildRequires:	kf5xmlgui-devel
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
Console that helps to debug akonadi

%files
%{_kde5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_kde5_bindir}/akonadiconsole
%{_kde5_datadir}/kconf_update/akonadiconsole*
%{_kde5_iconsdir}/hicolor/*/apps/akonadiconsole.*
%{_kde5_sysconfdir}/xdg/akonadiconsole.categories
%{_kde5_sysconfdir}/xdg/akonadiconsole.renamecategories

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

