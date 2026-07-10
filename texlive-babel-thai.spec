%global tl_name babel-thai
%global tl_revision 30564

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Support for Thai within babel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/thai
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-thai.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for typesetting Thai text. within the babel
system.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-thai
%dir %{_datadir}/texmf-dist/source/generic/babel-thai
%dir %{_datadir}/texmf-dist/tex/generic/babel-thai
%doc %{_datadir}/texmf-dist/doc/generic/babel-thai/thai.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-thai/thai.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-thai/thai.ins
%{_datadir}/texmf-dist/tex/generic/babel-thai/lthenc.def
%{_datadir}/texmf-dist/tex/generic/babel-thai/thai.ldf
%{_datadir}/texmf-dist/tex/generic/babel-thai/tis620.def
