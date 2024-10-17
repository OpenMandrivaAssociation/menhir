%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Menhir is a LR(1) parser generator for OCaml
Name:		menhir
Version:	20130911
Release:	3
License:	LGPL and QPL with static compilation exception
Group:		Development/Other
Url:		https://pauillac.inria.fr/~fpottier/menhir/
Source0:	http://pauillac.inria.fr/~fpottier/menhir/menhir-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Menhir is a LR(1) parser generator for OCaml. It is mostly compatible
with the standard ocamlyacc and has the following enhancements:

- it accepts LR(1) grammars,
- it offers parameterized nonterminal symbols as well as a library of
  standard definitions,
- it explains conflicts in terms of the grammar,
- it allows grammar specifications to be split over multiple files and
  parametrized by OCaml modules,
- it produces reentrant parsers.

%files
%doc manual.pdf
%{_bindir}/menhir
%{_mandir}/man1/menhir.1*
%{_datadir}/menhir/standard.mly
%dir %{_libdir}/ocaml/menhirLib
%{_libdir}/ocaml/menhirLib/*.cmi
%{_libdir}/ocaml/menhirLib/*.cmo
%{_libdir}/ocaml/menhirLib/*.o
%{_libdir}/ocaml/menhirLib/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc demos/
%{_libdir}/ocaml/menhirLib/*.cmx

#----------------------------------------------------------------------------

%prep
%setup -q

%build
# PREFIX is there without %{buildroot} because it is used to write the
# lib path in the source
make PREFIX=/usr

%install
# Prevent recompilation when doing make install
sed -i 's/install: all/install:/' Makefile
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR/menhirLib
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install PREFIX=%{buildroot}/usr

