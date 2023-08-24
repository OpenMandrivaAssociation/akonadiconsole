%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Console that helps to debug akonadi
Name:		akonadiconsole
Version:	23.08.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KPim5Akonadi)
BuildRequires:	cmake(KPim5AkonadiSearch)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KPim5AkonadiContact)
BuildRequires:	cmake(KPim5CalendarSupport)
BuildRequires:	cmake(KPim5AkonadiMime)
BuildRequires:	cmake(KPim5IMAP)
BuildRequires:	cmake(KPim5MessageViewer)
BuildRequires:	cmake(KPim5Mime)
BuildRequires:	cmake(KPim5Libkdepim)
BuildRequires:	cmake(KPim5Libkleo)
BuildRequires:	cmake(QGpgme)
BuildRequires:	pkgconfig(xapian-core)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	boost-devel

%description
Console that helps to debug akonadi.

%libpackage akonadiconsole 5

%files -f akonadiconsole.lang
%{_kde5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_bindir}/akonadiconsole
%{_iconsdir}/hicolor/*/apps/akonadiconsole.*
%{_datadir}/qlogging-categories5/akonadiconsole.categories
%{_datadir}/qlogging-categories5/akonadiconsole.renamecategories

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadiconsole
