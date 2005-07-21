# TODO
# - subpackages
# - everything
Summary:	eGroupWare - a web-based groupware suite written in PHP
Summary(pl):	eGroupWAre - oparte na WWW oprogramowanie do pracy grupowej napisane w PHP
Name:		egroupware
Version:	1.0.0.008
%define	_rel 2
Release:	0.%{_rel}.1
Epoch:		0
License:	GPL
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/egroupware/eGroupWare-%{version}-%{_rel}.tar.bz2
# Source0-md5:	30984ed46fa064632a3f3a1137786cbd
URL:		http://www.egroupware.org/
Requires:	php >= 3:4.1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir %{_datadir}/%{name}

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
install -d $RPM_BUILD_ROOT%{_appdir}

cp -a *.php $RPM_BUILD_ROOT%{_appdir}
cp -a addressbook admin backup bookmarks calendar comic developer_tools \
email emailadmin etemplate felamimail filemanager forum ftp fudforum headlines \
infolog jinn manual messenger news_admin phpbrain phpgwapi phpldapadmin \
phpsysinfo polls preferences projects registration setup sitemgr stocks tts \
wiki $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_appdir}
