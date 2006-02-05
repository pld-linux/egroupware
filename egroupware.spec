# TODO
# - subpackages for applications
# - separate htdocs and includedirs
# - list of bundled software (to use pld packages instead):
# - everything

%define	_rc RC6
%define	_rel 0.1
Summary:	eGroupWare - a web-based groupware suite written in PHP
Summary(pl):	eGroupWAre - oparte na WWW oprogramowanie do pracy grupowej napisane w PHP
Name:		egroupware
Version:	1.2
Release:	1.%{_rc}.%{_rel}
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/egroupware/eGroupWare-%{version}%{_rc}-2.tar.bz2
# Source0-md5:	f86c82871c1c6158ee7cfc80996c6d9d
Source1:	%{name}.conf
Patch0:		%{name}-setup.patch
Patch1:		%{name}-ttfdir.patch
URL:		http://www.egroupware.org/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires:	%{name}(DB_Driver) = %{version}-%{release}
Requires:	fonts-TTF-bitstream-vera
Requires:	php >= 3:4.1.2
Requires:	php-cli
Requires:	php-gd
Requires:	php-mbstring
Requires:	php-pcre
Requires:	webapps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%define		_noautoreqfiles	/usr/bin/php

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

%package setup
Summary:	eGroupware setup package
Summary(pl):	Pakiet do wstêpnej konfiguracji eGroupware
Group:		Applications/WWW
Requires:	%{name} = %{version}-%{release}

%description setup
Install this package to configure initial eGroupware installation. You
should uninstall this package when you're done, as it considered
insecure to keep the setup files in place.

%description setup -l pl
Ten pakiet nale¿y zainstalowaæ w celu wstêpnej konfiguracji eGroupware
po pierwszej instalacji. Potem nale¿y go odinstalowaæ, jako ¿e
pozostawienie plików instalacyjnych mog³oby byæ niebezpieczne.

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
# undos the sources
find -regex '.*\.\(php\|inc\|html\|txt\|js\)$' -print0 | xargs -0 sed -i -e 's,\r$,,'

%patch0 -p1
%patch1 -p1

# GPL
rm doc/LICENSE

# no need.
rm -r doc/rpm-build

# using PLD package
rm -r projectmanager/inc/ttf-bitstream-vera-1.10

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a */ $RPM_BUILD_ROOT%{_appdir}

> $RPM_BUILD_ROOT%{_sysconfdir}/header.php
ln -s %{_sysconfdir}/header.php $RPM_BUILD_ROOT%{_appdir}/header.inc.php

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf

# needed by setup script
install header.inc.php.template $RPM_BUILD_ROOT%{_appdir}

rm -rf $RPM_BUILD_ROOT%{_appdir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1
%webapp_register apache %{_webapp}

%triggerun -- apache1
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerpostun -- %{name} < 1.2-1.RC6.0.1
# rescue app configs
if [ -f /etc/%{name}/header.php.rpmsave ]; then
	mv -f %{_sysconfdir}/header.php{,.rpmnew}
	mv -f /etc/%{name}/header.php.rpmsave %{_sysconfdir}/$i
fi

# migrate from apache-config macros
if [ -f /etc/%{name}/apache.conf.rpmsave ]; then
	if [ -d /etc/apache/webapps.d ]; then
		cp -f %{_sysconfdir}/apache.conf{,.rpmnew}
		cp -f /etc/%{name}/apache.conf.rpmsave %{_sysconfdir}/apache.conf
	fi

	if [ -d /etc/httpd/webapps.d ]; then
		cp -f %{_sysconfdir}/httpd.conf{,.rpmnew}
		cp -f /etc/%{name}/apache.conf.rpmsave %{_sysconfdir}/httpd.conf
	fi
	rm -f /etc/%{name}/apache.conf.rpmsave
fi

# migrating from earlier apache-config?
if [ -L /etc/apache/conf.d/99_%{name}.conf ]; then
	rm -f /etc/apache/conf.d/99_%{name}.conf
	/usr/sbin/webapp register apache %{_webapp}
	%service -q apache reload
fi
if [ -L /etc/httpd/httpd.conf/99_%{name}.conf ]; then
	rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	/usr/sbin/webapp register httpd %{_webapp}
	%service -q httpd reload
fi

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/header.php
%doc doc/*
%dir %{_appdir}
%{_appdir}/*.php
%{_appdir}/addressbook
%{_appdir}/admin
%{_appdir}/bookmarks
%{_appdir}/calendar
%{_appdir}/developer_tools
%{_appdir}/emailadmin
%{_appdir}/etemplate
%{_appdir}/felamimail
%{_appdir}/filemanager
%{_appdir}/infolog
%{_appdir}/jinn
%{_appdir}/manual
%{_appdir}/news_admin
%{_appdir}/phpbrain
%{_appdir}/polls
%{_appdir}/preferences
%{_appdir}/registration
%{_appdir}/sitemgr
%{_appdir}/wiki
%{_appdir}/home
%{_appdir}/mydms
%{_appdir}/projectmanager
%{_appdir}/resources
%{_appdir}/sambaadmin
%{_appdir}/syncml
%{_appdir}/timesheet
%{_appdir}/workflow

%dir %{_appdir}/phpgwapi
%{_appdir}/phpgwapi/*.php
%{_appdir}/phpgwapi/cron
%{_appdir}/phpgwapi/doc
%{_appdir}/phpgwapi/inc
%{_appdir}/phpgwapi/js
%{_appdir}/phpgwapi/setup
%{_appdir}/phpgwapi/templates
%{_appdir}/phpgwapi/themes
%{_appdir}/phpgwapi/tests
%dir %attr(775,root,http) %{_appdir}/phpgwapi/images
%{_appdir}/phpgwapi/images/*

%files setup
%defattr(644,root,root,755)
%{_appdir}/header.inc.php.template
%{_appdir}/setup

%files db-mysql
%defattr(644,root,root,755)

%files db-pgsql
%defattr(644,root,root,755)

%files db-mssql
%defattr(644,root,root,755)
