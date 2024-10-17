Name:		texlive-babel-thai
Version:	30564
Release:	2
Summary:	Support for Thai within babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/thai
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for typesetting Thai text. within
the babel system.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-thai/lthenc.def
%{_texmfdistdir}/tex/generic/babel-thai/thai.ldf
%{_texmfdistdir}/tex/generic/babel-thai/tis620.def
%doc %{_texmfdistdir}/doc/generic/babel-thai/thai.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-thai/thai.dtx
%doc %{_texmfdistdir}/source/generic/babel-thai/thai.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
