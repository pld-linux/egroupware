# TODO
# - separate htdocs and includedirs
# - list of bundled software (to use pld packages instead):
# - everything

%define	_rel 0.23
Summary:	eGroupWare - a web-based groupware suite written in PHP
Summary(pl):	eGroupWAre - oparte na WWW oprogramowanie do pracy grupowej napisane w PHP
Name:		egroupware
Version:	1.2
Release:	2.%{_rel}
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/egroupware/eGroupWare-%{version}-2.tar.bz2
# Source0-md5:	2758792188125086f815e0e412a30904
Source1:	http://dl.sourceforge.net/egroupware/eGroupWare-contrib-%{version}-2.tar.bz2
# Source1-md5:	574b71590449f7650aecd61cda496aec
Source2:	%{name}.conf
Source3:	%{name}.cron
Patch0:		%{name}-setup.patch
Patch1:		%{name}-ttfdir.patch
URL:		http://www.egroupware.org/
BuildRequires:	rpmbuild(macros) >= 1.304
BuildRequires:	sed >= 4.0
Requires:	%{name}-addressbook = %{version}-%{release}
Requires:	%{name}-bookmarks = %{version}-%{release}
Requires:	%{name}-calendar = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-developer_tools = %{version}-%{release}
Requires:	%{name}-emailadmin = %{version}-%{release}
Requires:	%{name}-felamimail = %{version}-%{release}
Requires:	%{name}-filemanager = %{version}-%{release}
Requires:	%{name}-infolog = %{version}-%{release}
Requires:	%{name}-manual = %{version}-%{release}
Requires:	%{name}-mydms = %{version}-%{release}
Requires:	%{name}-news_admin = %{version}-%{release}
Requires:	%{name}-phpbrain = %{version}-%{release}
Requires:	%{name}-polls = %{version}-%{release}
Requires:	%{name}-projectmanager = %{version}-%{release}
Requires:	%{name}-registration = %{version}-%{release}
Requires:	%{name}-resources = %{version}-%{release}
Requires:	%{name}-sambaadmin = %{version}-%{release}
Requires:	%{name}-sitemgr = %{version}-%{release}
Requires:	%{name}-syncml = %{version}-%{release}
Requires:	%{name}-timesheet = %{version}-%{release}
Requires:	%{name}-wiki = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}
%define		schemadir	/usr/share/openldap/schema

%description
eGroupWare is a multi-user, web-based groupware suite developed on a
custom set of PHP-based APIs.

This package provides the eGroupWare default applications:

egroupware core with: admin, api, docs, etemplate, preferences,
addressbook, bookmarks, calendar, translation-tools, emailadmin,
felamimail, filemanager, infolog, manual, mydms, news admin,
knowledgebase, polls, projectmanager, resources, sambaadmin, sitemgr,
syncml, timesheet, wiki, workflow

It also provides an API for developing additional applications.

Further contributed applications are avalible in single packages.

%description -l pl
eGroupWare to wielou¿ytkownikowe, oparte na WWW oprogramowanie do
pracy grupowej stworzone na w³asnym zestawie API opartych na PHP.
Aktualnie dostêpne modu³y obejmuj±: pocztê elektroniczn±, ksi±¿kê
adresow±, kalendarz, infolog (notatki, rzeczy do zrobienia, rozmowy
telefoniczne), zarz±dzanie tre¶ci±, forum, zak³adki, wiki.

%package core
Summary:	The eGroupWare core package
Group:		Applications/WWW
Requires:	%{name}(DB_Driver) = %{version}-%{release}
Requires:	/usr/bin/php
Requires:	crondaemon
Requires:	fonts-TTF-bitstream-vera
Requires:	php-cli
Requires:	php(gd)
Requires:	php(imap)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	webapps
Requires:	webserver(php) >= 4.3
Provides:	%{name}-etemplate = %{version}-%{release}
Provides:	%{name}-syncml = %{version}-%{release}

%description core
This package provides the eGroupWare core applications.

%package addressbook
Summary:	The eGroupWare addressbook application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description addressbook
Contact manager with Vcard support. addressbook is the egroupware
default contact application. It makes use of the egroupware contacts
class to store and retrieve contact information via SQL, LDAP or
Active Directory.

%package backup
Summary:	The eGroupWare backup application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description backup
An online configurable backup app to store data offline. Can store
files in zip, tar.gz and tar.bz2 on the local machine or Remote via
FTP, SMBMOUNT or NFS

%package browser
Summary:	The eGroupWare browser application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description browser
Intergrated browser to surf the web within eGroupWare.

%package bookmarks
Summary:	The eGroupWare bookmarks application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description bookmarks
Manage your bookmarks with eGroupWare. Has Netscape plugin.

%package calendar
Summary:	The eGroupWare calendar application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-etemplate = %{version}-%{release}

%description calendar
Powerful calendar with meeting request system, Alarms, ICal and E-Mail
support, and ACL security.

%package chatty
Summary:	Instant messenger for eGroupWare
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description chatty
Instant messenger application using AJAX.

%package comic
Summary:	The eGroupWare comic application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description comic
This application display comic strips.

%package developer_tools
Summary:	The eGroupWare developer_tools application
Group:		Applications/WWW

%description developer_tools
The TranslationTools allow to create and extend translations-files for
eGroupWare. They can search the sources for new / added phrases and
show you the ones missing in your language.

%package email
Summary:	The eGroupWare email application
Group:		Applications/WWW
Requires:	%{name}-addressbook = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description email
AngleMail for eGroupWare at www.anglemail.org is an Email reader with
multiple accounts and mailbox filtering. Also Anglemail support IMAP,
IMAPS, POP3 and POP3S accounts.

%package emailadmin
Summary:	The eGroupWare emailadmin application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description emailadmin
EmailAdmin allow to maintain User email accounts

%package egwical
Summary:	The eGroupWare egwical application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description egwical
This is the egwical app for eGroupWare.

%package felamimail
Summary:	The eGroupWare felamimail application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-emailadmin = %{version}-%{release}

%description felamimail
The felamimail Email Reader is a other Email application for
eGroupWare.

%package filemanager
Summary:	The eGroupWare filemanager application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description filemanager
This is the filemanager app for eGroupWare.

%package filescenter
Summary:	The eGroupWare filescenter application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description filescenter
This is the filescenter app for eGroupWare.

%package forum
Summary:	The eGroupWare forum application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description forum
This is the forum app for eGroupWare.

%package ftp
Summary:	The eGroupWare ftp application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description ftp
This is the ftp app for eGroupWare.

%package fudforum
Summary:	The eGroupWare fudforum application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description fudforum
This is the fudforum app for eGroupWare.

%package headlines
Summary:	The eGroupWare headlines application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description headlines
This is the headlines app for eGroupWare.

%package icalsrv
Summary:	The eGroupWare icalsrv application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description icalsrv
This is the icalsrv app for eGroupWare.

%package infolog
Summary:	The eGroupWare infolog application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-etemplate = %{version}-%{release}

%description infolog
This is the infolog app for eGroupWare (Notes, ToDo, Phonelogs, CRM).

%package jinn
Summary:	The eGroupWare jinn application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description jinn
The jinn app is a multi-site, multi-database, multi-user/-group,
database driven Content Management System written in and for the
eGroupWare Framework.

%package manual
Summary:	The eGroupWare manual application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description manual
This is the manual app for eGroupWare: online help system.

%package messenger
Summary:	The eGroupWare messenger application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description messenger
This is the messenger app for eGroupWare.

%package mydms
Summary:	The eGroupWare mydms application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description mydms
This is a mydms port to eGroupWare.

%package news_admin
Summary:	The eGroupWare news_admin application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description news_admin
This is the news_admin app for eGroupWare.

%package phpbrain
Summary:	The eGroupWare phpbrain application
Group:		Applications/WWW
Requires:	%{name}-addressbook = %{version}-%{release}
Requires:	%{name}-core = %{version}-%{release}

%description phpbrain
This is the phpbrain app for eGroupWare.

%package phpldapadmin
Summary:	The eGroupWare phpldapadmin application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description phpldapadmin
This is the cire phpldapadmin of eGroupWare.

%package phpsysinfo
Summary:	The eGroupWare phpsysinfo application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description phpsysinfo
This is the phpsysinfo app for eGroupWare.

%package polls
Summary:	The eGroupWare polls application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description polls
This is the polls app for eGroupWare.

%package projectmanager
Summary:	The eGroupWare projectmanager application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-etemplate = %{version}-%{release}

%description projectmanager
The projectmanager is eGroupWare's new project management application.
It's fully integrated into eGroupWare and use the data of InfoLog and
Calendar. Plugable datasources allow to support and manage further
applications.

%package projects
Summary:	The eGroupWare projects application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-infolog = %{version}-%{release}

%description projects
This is the projects app for eGroupWare.

%package registration
Summary:	The eGroupWare registration application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description registration
This is the registration app for eGroupWare.

%package resources
Summary:	The eGroupWare resources application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-etemplate = %{version}-%{release}

%description resources
resources is a resource booking sysmtem for eGroupWare. Which
integrates into the calendar.

%package sambaadmin
Summary:	The eGroupWare sambaadmin application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description sambaadmin
Manage LDAP based sambaacounts and workstations.

%package sitemgr
Summary:	The eGroupWare Sitemanager CMS application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description sitemgr
This is the Sitemanager CMS app for eGroupWare.

%package stocks
Summary:	The eGroupWare stocks application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description stocks
This is the stocks app for eGroupWare.

%package timesheet
Summary:	The eGroupWare timesheet application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}
Requires:	%{name}-etemplate = %{version}-%{release}

%description timesheet
Simple timesheet application, which allow to record and report the
times and other expenses. It can be uses as well standalone as
together with the ProjectManager application.

%package tts
Summary:	The eGroupWare trouble ticket system application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description tts
This is the trouble ticket system} app for eGroupWare.

%package wiki
Summary:	The eGroupWare wiki application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description wiki
This is the wiki app for eGroupWare.

%package workflow
Summary:	The eGroupWare workflow application
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

%description workflow
This is the workflow app for eGroupWare.

%package setup
Summary:	eGroupware setup package
Summary(pl):	Pakiet do wstêpnej konfiguracji eGroupware
Group:		Applications/WWW
Requires:	%{name}-core = %{version}-%{release}

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
Requires:	php(mysql)
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-mysql
This virtual package provides MySQL database backend for eGroupware.

You will need MySQL server >= 4.0 to use this driver.

%description db-mysql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych MySQL dla
eGroupware.

%package db-pgsql
Summary:	eGroupware DB Driver for PostgreSQL
Summary(pl):	Sterownik bazy danych eGroupware dla PostgreSQL-a
Group:		Applications/WWW
Requires:	php(pgsql)
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
Requires:	php(mssql)
Provides:	%{name}(DB_Driver) = %{version}-%{release}

%description db-mssql
This virtual package provides MS SQL database backend for eGroupware.

%description db-mssql -l pl
Ten wirtualny pakiet dostarcza backend bazy danych MS SQL dla
eGroupware.

%package -n openldap-schema-egroupware
Summary:	eGroupWare LDAP schemas
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers
Requires:	sed >= 4.0

%description -n openldap-schema-egroupware
This package contains phpgwaccount.schema and phpgwcontact.schema for
openldap.

%prep
%setup -q -n %{name} -a1
mv %{name}/* .

# remove as did upstream
rm -rf rpc.php
rm -rf xmlrpc
rm -rf switchuser
rm -rf skel
rm -rf soap

# remove CVS control files
find -name .svn -print0 | xargs -0 rm -rf
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

# support just OpenLDAP
mv phpgwapi/doc/ldap/phpgw{account,contact}.schema .
mv phpgwapi/doc/ldap/README README.ldap
rm -rf phpgwapi/doc/ldap

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir},/var/{lib/%{name}/default/{files,backup},run/%{name}}}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a */ $RPM_BUILD_ROOT%{_appdir}

> $RPM_BUILD_ROOT%{_sysconfdir}/header.php
ln -s %{_sysconfdir}/header.php $RPM_BUILD_ROOT%{_appdir}/header.inc.php

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
install -D %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}

# needed by setup script
install header.inc.php.template $RPM_BUILD_ROOT%{_appdir}

# LDAP Schemas
install -d $RPM_BUILD_ROOT%{schemadir}
cp -a *.schema $RPM_BUILD_ROOT%{schemadir}

rm -rf $RPM_BUILD_ROOT%{_appdir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin core -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun core -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin core -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun core -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%post -n openldap-schema-egroupware
%openldap_schema_register %{schemadir}/phpgw{account,contact}.schema
%service -q ldap restart

%postun -n openldap-schema-egroupware
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/phpgw{account,contact}.schema
	%service -q ldap restart
fi

%files
%defattr(644,root,root,755)
%doc doc/* README.ldap

%files core
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(660,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/header.php
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%dir %{_appdir}
%{_appdir}/*.php

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

# maybe separate these apps?
%{_appdir}/syncml
%{_appdir}/admin
%{_appdir}/etemplate
%{_appdir}/preferences
%{_appdir}/home

%dir /var/lib/%{name}/default
%dir %attr(775,root,http) /var/lib/%{name}/default/backup
%dir %attr(775,root,http) /var/lib/%{name}/default/files
%dir %attr(775,root,http) /var/run/%{name}

%files addressbook
%defattr(644,root,root,755)
%{_appdir}/addressbook

%files backup
%defattr(644,root,root,755)
%{_appdir}/backup

%files bookmarks
%defattr(644,root,root,755)
%{_appdir}/bookmarks

%files browser
%defattr(644,root,root,755)
%{_appdir}/browser

%files calendar
%defattr(644,root,root,755)
%{_appdir}/calendar

%files chatty
%defattr(644,root,root,755)
%{_appdir}/chatty

%files comic
%defattr(644,root,root,755)
%{_appdir}/comic

%files developer_tools
%defattr(644,root,root,755)
%{_appdir}/developer_tools

%files email
%defattr(644,root,root,755)
%{_appdir}/email

%files emailadmin
%defattr(644,root,root,755)
%{_appdir}/emailadmin

%files egwical
%defattr(644,root,root,755)
%{_appdir}/egwical

%files felamimail
%defattr(644,root,root,755)
%{_appdir}/felamimail

%files filemanager
%defattr(644,root,root,755)
%{_appdir}/filemanager

%files filescenter
%defattr(644,root,root,755)
%{_appdir}/filescenter

%files forum
%defattr(644,root,root,755)
%{_appdir}/forum

%files ftp
%defattr(644,root,root,755)
%{_appdir}/ftp

%files fudforum
%defattr(644,root,root,755)
%{_appdir}/fudforum

%files headlines
%defattr(644,root,root,755)
%{_appdir}/headlines

%files icalsrv
%defattr(644,root,root,755)
%{_appdir}/icalsrv

%files infolog
%defattr(644,root,root,755)
%{_appdir}/infolog

%files jinn
%defattr(644,root,root,755)
%{_appdir}/jinn

%files manual
%defattr(644,root,root,755)
%{_appdir}/manual

%files messenger
%defattr(644,root,root,755)
%{_appdir}/messenger

%files mydms
%defattr(644,root,root,755)
%{_appdir}/mydms

%files news_admin
%defattr(644,root,root,755)
%{_appdir}/news_admin

%files phpbrain
%defattr(644,root,root,755)
%{_appdir}/phpbrain

%files phpldapadmin
%defattr(644,root,root,755)
%{_appdir}/phpldapadmin

%files phpsysinfo
%defattr(644,root,root,755)
%{_appdir}/phpsysinfo

%files polls
%defattr(644,root,root,755)
%{_appdir}/polls

%files projectmanager
%defattr(644,root,root,755)
%{_appdir}/projectmanager

%files projects
%defattr(644,root,root,755)
%{_appdir}/projects

%files registration
%defattr(644,root,root,755)
%{_appdir}/registration

%files resources
%defattr(644,root,root,755)
%{_appdir}/resources

%files sambaadmin
%defattr(644,root,root,755)
%{_appdir}/sambaadmin

%files sitemgr
%defattr(644,root,root,755)
%{_appdir}/sitemgr

%files stocks
%defattr(644,root,root,755)
%{_appdir}/stocks

%files timesheet
%defattr(644,root,root,755)
%{_appdir}/timesheet

%files tts
%defattr(644,root,root,755)
%{_appdir}/tts

%files wiki
%defattr(644,root,root,755)
%{_appdir}/wiki

%files workflow
%defattr(644,root,root,755)
%{_appdir}/workflow

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

%files -n openldap-schema-egroupware
%defattr(644,root,root,755)
%{schemadir}/phpgwaccount.schema
%{schemadir}/phpgwcontact.schema
