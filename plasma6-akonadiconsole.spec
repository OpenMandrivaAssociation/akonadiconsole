#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Console that helps to debug akonadi
Name:		plasma6-akonadiconsole
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/akonadiconsole/-/archive/%{gitbranch}/akonadiconsole-%{gitbranchd}.tar.bz2#/akonadiconsole-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/akonadiconsole-%{version}.tar.xz
%endif

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6AkonadiSearch)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KPim6CalendarSupport)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KPim6MessageViewer)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6Libkleo)
BuildRequires:	cmake(QGpgme)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(xapian-core)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(libsasl2)
BuildRequires:	boost-devel

%description
Console that helps to debug akonadi.

%files -f akonadiconsole.lang
%{_datadir}/applications/org.kde.akonadiconsole.desktop
%{_bindir}/akonadiconsole
%{_iconsdir}/hicolor/*/apps/akonadiconsole.*
%{_datadir}/qlogging-categories6/akonadiconsole.categories
%{_datadir}/qlogging-categories6/akonadiconsole.renamecategories
%{_libdir}/libakonadiconsole.so*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n akonadiconsole-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang akonadiconsole
