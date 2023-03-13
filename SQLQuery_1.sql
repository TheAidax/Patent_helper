DROP TABLE documents
DROP TABLE patents
DROP TABLE cip

CREATE TABLE documents(id INT IDENTITY(1, 1) PRIMARY KEY, patentNum INTEGER, document BINARY)
CREATE TABLE patents(id INT IDENTITY(1, 1) PRIMARY KEY, patentNum INTEGER, patentApplicationNum INTEGER, continuityData INTEGER)


CREATE TABLE cip(id INT IDENTITY(1, 1) PRIMARY KEY, patentNum INTEGER, cipApplicationNum INTEGER, continuityData INTEGER)

