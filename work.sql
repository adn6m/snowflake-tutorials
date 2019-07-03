use warehouse sf_tuts_wh;

use database sf_tuts;



create or replace table information (
                                      first_name string ,
                                      last_name string ,
                                      email string ,
                                      streetaddress string ,
                                      city string ,
                                      start_date date
                                      );

copy into information
from s3://sevenone credentials=(aws_key_id='REDACTED' aws_secret_key='REDACTED')
file_format = (type = csv field_optionally_enclosed_by='"')
pattern = '.*employees0[1-5].csv'
on_error = 'skip_file';


create or replace function name2()
  returns table (email string, city string)
  as
  $$
    select email, city from information
  $$
  ;
select * from table (name2());