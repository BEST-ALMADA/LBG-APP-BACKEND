DROP TABLE eventos cascade constraints; 

DROP TABLE empresas cascade constraints; 

DROP TABLE documentos cascade constraints; 

--DROP TABLE internos cascade constraints; 

--DROP TABLE externos cascade constraints; 

DROP TABLE equipas cascade constraints; 

DROP TABLE cargos cascade constraints; 

DROP TABLE mandatos cascade constraints; 

DROP TABLE pessoas cascade constraints; 

DROP TABLE membros cascade constraints; 

DROP TABLE participantes cascade constraints; 

DROP TABLE participacoes cascade constraints; 

 

-- Criacao de tabelas 

CREATE TABLE eventos ( 

	idEquipa number(4), 

	idEvento number(4), 

nome varchar2(30), 

descricao varchar2(200), 

numTotalParticipantes number(4), 

numAtualParticipantes number(4), 

numAtualOrganizers number(4), 

dataInicio date, 

dataFim date, 

); 

 

CREATE TABLE empresas( 

idEmpresa number(4), 

nome varchar2(30), 

dinheiroFinanciado number(5), 

); 

 

CREATE TABLE documentos( 

	IdDocumento number(6), 

	tipo varchar2(10), 

nome varchar2(50), 

descricao varchar2(200), 

dataCriacao Date, 

localizacao varchar2(200), 

); 

 

CREATE TABLE equipas( 

	idEquipa number(2), 

	nome varchar2(10), 

	numMembros number(2), 

); 

 

CREATE TABLE cargos( 

idCargo number(3), 

nome varchar2(30), 

descricao varchar2(100),  

); 

 

CREATE TABLE mandatos( 

	idCargo number(3), 

email varchar2(50), 

dataInicio date, 

dataFim date. 

); 

 

CREATE TABLE pessoas( 

	email varchar2(50), 

	descricao varchar2(200), 

	nome varchar2(100), 

	alcunha varchar2(25), 

	dataNascimento date, 

	idade number(2), 

	telemovel number(15), 

	tamanho 

	 

); 

 

CREATE TABLE membros( 

	membership varchar2(10), 

	dataEntrada date, 

	tempoLBGSemestres number(2), 

historicoCargos varchar2(1000), 

foto varbinary(max), 

); 

 

CREATE TABLE participantes( 

	dataExpiracaoDoc date, 

contactoEmerg number(15), 

dieta varchar2(30), 

ultimaDataLogin date 

); 

 

CREATE TABLE participacoes( 

	IdEvento number(4), 

email varchar2(30), 

dataInscricao date 

); 

 

 

-- Chaves primarias 

alter table evento add constraint pk_eve primary key(idEquipa, idEvento); 

alter table empresas add constraint pk_emp primary key(idEmpresa); 

alter table documentos add constraint pk_doc primary key(idDocumentos); 

alter table equipas add constraint pk_eqp primary key(idEquipa); 

alter table cargos add constraint pk_crg primary key(idCargo); 

alter table pessoas add constraint pk_pes primary key(email); 

alter table participacoes add constraint pk_pla primary key(idEvento, email); 
