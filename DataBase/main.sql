drop database LBGAPP;

Create database LBGAPP;
USE LBGAPP;

-- Criacao de tabelas 

	CREATE TABLE eventos (

		idEquipaEvento int(4), 

		idEvento int(4), 

		nome varchar(30), 

		descricao varchar(2000), 

		numTotalParticipantes int(4), 

		numAtualParticipantes int(4), 

		dataInicio date, 

		dataFim date,

		sponsors varchar(100),

		contactosCoordenacao varchar(100)

	);

	CREATE TABLE cargosEventos( 

		idCargoEvento int(3),

		nome varchar(30),

		descricao varchar(200)

	); 


	CREATE TABLE equipasEventos(

		idEquipaEvento int(3),

		nome varchar(30),

		numMembros int(2)

	); 


	CREATE TABLE empresas( 

		idEmpresa int(4), 

		nome varchar(30), 

		dinheiroFinanciado int(5),

		categoria varchar(80)

	); 
		

	CREATE TABLE documentos( 

		idDocumento int(6), 

		tipo varchar(10), 

		nome varchar(50),

		descricao varchar(200),

		dataCriacao date,

		localizacao varchar(200)

	); 


	CREATE TABLE equipas( 

		idEquipa int(2),

		nome varchar(20),

		numMembros int(2)

	);


	CREATE TABLE cargos( 

		idCargo int(3),

		nome varchar(30),

		descricao varchar(200)

	); 


	CREATE TABLE mandatos( 

		idCargo int(3), 

		email varchar(50), 

		dataInicio date, 

		dataFim date,

		primary key (idCargo,email,dataInicio)

	); 


	CREATE TABLE pessoas( 

		email varchar(50),

		descricao varchar(200),

		nome varchar(100),

		alcunha varchar(25),

		dataNascimento date,

		password varchar(1024),

		telemovel int(15),

		tamanho varchar(8)

	); 

		
	CREATE TABLE membros( 

		email varchar(50),

		membership varchar(10),

		dataEntrada date,

		tempoLBGSemestres int(2),

		foto varchar(4096),

		primary key (email)

	); 


	CREATE TABLE participantes( 

		email varchar(50),

		dataExpiracaoDoc date,

		contactoEmerg int(15),

		dieta varchar(30),

		ultimaDataLogin date,

		primary key (email)

	); 

		
	CREATE TABLE participacoes( 

		IdEvento int(4),

		email varchar(30),

		dataInscricao date

	); 
		

	-- Chaves primarias 

	alter table empresas add constraint pk_emp primary key(idEmpresa);

	alter table documentos add constraint pk_doc primary key(idDocumento);

	alter table eventos add constraint pk_eve primary key(idEvento);

	alter table equipas add constraint pk_eqp primary key(idEquipa);

	alter table cargos add constraint pk_crg primary key(idCargo);

	alter table equipasEventos add constraint pk_eqp_eve primary key(idEquipaEvento);

	alter table cargosEventos add constraint pk_crg_eve primary key(idCargoEvento);

	alter table pessoas add constraint pk_pes primary key(email);

	alter table participacoes add constraint pk_pla primary key(idEvento, email);


	-- Chaves foreign
	
	alter table membros add constraint fk_memb foreign key (email) references pessoas(email);

	alter table participantes add constraint fk_part foreign key (email) references pessoas(email);
		
	alter table participacoes add constraint fk_part_oes_ento foreign key (idEvento) references eventos(idEvento);

	alter table participacoes add constraint fk_part_oes_mail foreign key (email) references pesosas(email);

	alter table eventos add constraint fk_eve_equ foreign key (idEquipaEvento) references equipasEventos(idEquipaEvento);

	alter table mandatos add constraint fk_mand_carg foreign key (idCargo) references cargos(idCargo);