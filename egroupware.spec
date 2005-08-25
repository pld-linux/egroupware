# TODO
# - subpackages
# - everything
Summary:	eGroupWare - a web-based groupware suite written in PHP
Summary(pl):	eGroupWAre - oparte na WWW oprogramowanie do pracy grupowej napisane w PHP
Name:		egroupware
Version:	1.0.0.009
Release:	0.4
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/egroupware/eGroupWare-%{version}.tar.bz2
# Source0-md5:	2ed2f3041ab4ff235f56ed23dfa7274b
Source1:	%{name}.conf
URL:		http://www.egroupware.org/
Requires:	php >= 3:4.1.2
Requires:	php-mysql
Requires:	php-pgsql
#Requires:	php(pgsql||mysql) <- that would be neat
Requires:	php-pcre
Requires:	php-gd
Requires:	php-mbstring
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
%{_appdir}
