# TODO
# - subpackages
# - everything
Summary:	eGroupWare - a web-based groupware suite written in PHP
Summary(pl):	eGroupWAre - oparte na WWW oprogramowanie do pracy grupowej napisane w PHP
Name:		egroupware
Version:	1.0.0.009
Release:	0.12
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/egroupware/eGroupWare-%{version}.tar.bz2
# Source0-md5:	2ed2f3041ab4ff235f56ed23dfa7274b
Source1:	%{name}.conf
URL:		http://www.egroupware.org/
Requires:	%{name}(DB_Driver)
Requires:	php >= 3:4.1.2
Requires:	php-gd
Requires:	php-mbstring
Requires:	php-pcre
Requires:	php-cli
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir %{_datadir}/%{name}
%define		_sysconfdir /etc/%{name}

%description
eGroupWare is a multi-user, web-based groupware suite developed on a
custom set of PHP-based APIs. Currently available modules include:
email, addressbook, calendar, infolog (notes, to-do's, phone calls),
content management, forum, bookmarks, wiki.

%description -l pl
eGroupWare to wielou¿ytkownikowe, oparte na WWW oprogramowanie do
pracy grupowej stworzone na w³asnym zestawie API opartych na PHP.
Aktualnie dostêpne modu³y obejmuj±: pocztê elektroniczn±, ksi±¿kê
adresow±, kalendarz, infolog (notatki, rzeczy do zrobienia, rozmowy
telefoniczne), zarz±dzanie tre¶ci±, forum, zak³adki, wiki.

%package db-mysql
Summary:	eGroupware DB Driver for MySQL
Summary(pl):	Sterownik bazy danych eGroupware dla MySQL-a
Group:		Applications/WWW
Requires:	php-mysql
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-mysql
This virtual package provides MySQL database backend for eGroupware.

%description db-mysql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych MySQL dla
eGroupware.

%package db-pgsql
Summary:	eGroupware DB Driver for PostgreSQL
Summary(pl):	Sterownik bazy danych eGroupware dla PostgreSQL-a
Group:		Applications/WWW
Requires:	php-pgsql
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-pgsql
This virtual package provides PostgreSQL database backend for
eGroupware.

%description db-pgsql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych PostgreSQL dla
eGroupware.

%package db-mssql
Summary:	eGroupware DB Driver for MS SQL
Summary(pl):	Sterownik bazy danych eGroupware dla MS SQL-a
Group:		Applications/WWW
Requires:	php-mssql
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-mssql
This virtual package provides MS SQL database backend for eGroupware.

%description db-mssql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych MS SQL dla
eGroupware.

%prep
%setup -q -n %{name}

# remove CVS control files
find -name CVS -print0 | xargs -0 rm -rf

# GPL
rm -f doc/LICENSE

# no need.
rm -rf doc/rpm-build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a addressbook admin backup bookmarks calendar comic developer_tools \
email emailadmin etemplate felamimail filemanager forum ftp fudforum headlines \
infolog jinn manual messenger news_admin phpbrain phpgwapi phpldapadmin \
phpsysinfo polls preferences projects registration setup sitemgr stocks tts \
wiki $RPM_BUILD_ROOT%{_appdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 >= 1.3.33-2
%apache_config_install -v 1 -c %{_sysconfdir}/apache.conf

%triggerun -- apache1 >= 1.3.33-2
%apache_config_uninstall -v 1

%triggerin -- apache >= 2.0.0
%apache_config_install -v 2 -c %{_sysconfdir}/apache.conf

%triggerun -- apache >= 2.0.0
%apache_config_uninstall -v 2

%files
%defattr(644,root,root,755)
%attr(710,root,http) %dir %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%doc doc/*
%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/addressbook
%{_appdir}/admin
%{_appdir}/backup
%{_appdir}/bookmarks
%{_appdir}/calendar
%{_appdir}/comic
%{_appdir}/developer_tools
%{_appdir}/email
%{_appdir}/emailadmin
%{_appdir}/etemplate
%{_appdir}/felamimail
%{_appdir}/filemanager
%{_appdir}/forum
%{_appdir}/ftp
%{_appdir}/headlines
%{_appdir}/infolog
%{_appdir}/jinn
%{_appdir}/manual
%{_appdir}/messenger
%{_appdir}/news_admin
%{_appdir}/phpbrain
%{_appdir}/phpldapadmin
%{_appdir}/phpsysinfo
%{_appdir}/polls
%{_appdir}/preferences
%{_appdir}/projects
%{_appdir}/registration
%{_appdir}/setup
%{_appdir}/sitemgr
%{_appdir}/stocks
%{_appdir}/tts
%{_appdir}/wiki

%dir %{_appdir}/phpgwapi
%{_appdir}/phpgwapi/*.php
%{_appdir}/phpgwapi/cron
%{_appdir}/phpgwapi/doc
%{_appdir}/phpgwapi/inc
%{_appdir}/phpgwapi/js
%{_appdir}/phpgwapi/setup
%{_appdir}/phpgwapi/templates
%{_appdir}/phpgwapi/themes
%dir %attr(775,root,http) %{_appdir}/phpgwapi/images
%{_appdir}/phpgwapi/images/*

%dir %attr(775,root,http) %{_appdir}/fudforum
%{_appdir}/fudforum/*.php
%{_appdir}/fudforum/inc
%{_appdir}/fudforum/setup
%{_appdir}/fudforum/templates

%files db-mysql
%defattr(644,root,root,755)

%files db-pgsql
%defattr(644,root,root,755)

%files db-mssql
%defattr(644,root,root,755)
