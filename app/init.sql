DROP TABLE IF EXISTS contact;
CREATE TABLE contact (
  contactId INT NOT NULL,
  firstName VARCHAR(50),
  lastName VARCHAR(50),
  phone VARCHAR(10),
  address VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(2),
  zip VARCHAR(5),
  PRIMARY KEY (contactId)
);