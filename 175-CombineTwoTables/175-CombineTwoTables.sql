-- Last updated: 8/11/2026, 12:33:41 PM
# Write your MySQL query statement below
select Person.firstName,Person.lastName,Address.city,Address.state from Person left join address on Person.personId = Address.personId;