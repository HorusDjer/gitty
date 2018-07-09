/*
THIS IS A COMPILATION OF QUERIES FOR QUICK TROUBLESHOOTING FOR COMMON PROBLEMS
TO SEE WHEN TO USE THESE QUERIES CHECK ERROR LOG TRACKER IN THE SOLUTION FIELD
*/

--QUERY 1 for troubleshooting
SELECT  countyname, precinctname, sum(weekly_walk_attempts) FROM (
select cc.statecode
    , di.countyname
    , di.precinctname
    , case 
        when cc.statecode='WI' and cc.datecanvassed::date <= '2018-04-03' then p.region_p1
        when cc.statecode='WI' and cc.datecanvassed::date > '2018-04-03' then p.region_p2
        when cc.statecode='OH' and cc.datecanvassed::date <= '2018-05-03' then p.region_p1
        when cc.statecode='OH' and cc.datecanvassed::date > '2018-05-03' then p.region_p2
        when cc.statecode='MI' and cc.datecanvassed::date<='2018-06-15' then p.region_p1_1
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-06-15' then p.region_p1_2
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-08-10' then p.region_p2
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-10-19' then p.region_p3
        when cc.statecode='WI' and cc.datecanvassed::date <= '2018-04-03' and p.region_p1 is null then 'Unturfed'
        when cc.statecode='WI' and cc.datecanvassed::date > '2018-04-03' and p.region_p2 is null then 'Unturfed'
        when cc.statecode='OH' and cc.datecanvassed::date <= '2018-05-03' and p.region_p1 is null then 'Unturfed'
        when cc.statecode='OH' and cc.datecanvassed::date > '2018-05-03' and p.region_p2 is null then 'Unturfed'
        when cc.statecode='MI' and cc.datecanvassed::date<='2018-06-15' and  p.region_p1_1 is null then 'Unturfed'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-06-15' and  p.region_p1_2 is null then 'Unturfed'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-08-10' and p.region_p2 is null then 'Unturfed'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-10-19' and p.region_p3 is null then 'Unturfed'
        when p.region_p1 is null then 'Unturfed'
        else p.region_p1 end as region
    , week_iso(date(cc.datecanvassed)-4) as week_iso --dates start monday so pull 4 days back to treat friday like monday.
    , max(cc.datecanvassed) as max_date_canvass
    , max(case 
        when cc.statecode='WI' and cc.datecanvassed::date <= '2018-04-03' then 'Phase 1'
        when cc.statecode='WI' and cc.datecanvassed::date > '2018-04-03' then 'Phase 2'
            when cc.statecode='OH' and cc.datecanvassed::date <= '2018-05-03' then 'Phase 1'
        when cc.statecode='OH' and cc.datecanvassed::date > '2018-05-03' then 'Phase 2'
            when cc.statecode='MI' and cc.datecanvassed::date<='2018-06-15' then 'Phase 1.1'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-06-15' then 'Phase 1.2'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-08-10' then 'Phase 2'
        when cc.statecode='MI' and cc.datecanvassed::date>'2018-10-19' then 'Phase 3'
        when p.region_p1 is null then 'Phase 1'
        else 'Phase 1' end  
    ) as phase --Not exact, some weeks will be both and this will  just favor phase 2 cause its a max
    , sum(case when c.contacttypename in ('Door to Door Canvass','Paid Walk', 'Walk','Phone') then 1 else 0 end) as weekly_attempts
    , sum(case when c.contacttypename in ('Door to Door Canvass','Paid Walk', 'Walk','Phone') and r.resultshortname = 'Canvassed' then 1 else 0 end) as weekly_convos
    , sum(case when c.contacttypename in ('Door to Door Canvass','Paid Walk', 'Walk') then 1 else 0 end) as weekly_walk_attempts
    , sum(case when c.contacttypename = 'Phone' then 1 else 0 end) as weekly_phone_attempts 
    , sum(case when c.contacttypename in ('Door to Door Canvass','Paid Walk', 'Walk') and r.resultshortname = 'Canvassed' then 1 else 0 end) as weekly_walk_convos
    , sum(case when c.contacttypename = 'Phone' and r.resultshortname = 'Canvassed' then 1 else 0 end) as weekly_phone_convos --resultid=14 and contacttypeid =1
    , sum(case when c.contacttypename in ('Door to Door Canvass','Paid Walk', 'Walk') and date(cc.datecanvassed) = current_date - 1 then 1 else 0 end) as yesterday_walk_attempts  
    , count(*) as num_responses
    from fof_vansync.contacts_contacts_vf cc
    left join fof_ablythe.person_best_region_vf p using (statecode, vanid) --note this is vf table
    left join fof_vansync.contact_types c using (contacttypeid) 
    left join fof_vansync.results r using (resultid)
    left join fof_vansync.dwid_to_van dw on cc.vanid=dw.vanid and cc.statecode=dw.statecode --lookup
    left join catalist_mdr.district_s di on di.state = dw.statecode and di.dwid = dw.dwid --their location info
    where cc.datecanvassed >= '2017-12-29' and cc.datecanvassed < current_date 
    --SUPRESS BLOC(CPD) 
    and ((cc.committeeid not in (50418) and cc.datecanvassed::date>'2018-04-03') or cc.datecanvassed::date<='2018-04-03')
    group by 1,2,3, 4, 5
    --find those in the unturfed region at a particular week
    ) x where region='Unturfed' and statecode='PA' and week_iso=24---and countyname='PHILADELPHIA'
    GROUP BY 1,2 order by 3 desc
    
-- QUERY 2 (checking latest canvass synced to database)
SELECT datecanvassed
FROM fof_vansync.contacts_contacts_vf
WHERE StateCode = 'NV'
ORDER BY datecanvassed DESC

-- QUERY 3 (checking for descrepancies with canvass count in VAN and Catalist by county)
SELECT ds.countyname, COUNT(ccv.DateCanvassed)
FROM fof_vansync.contacts_contacts_vf as ccv
LEFT JOIN fof_vansync.dwid_to_van as dtv
        on ccv.VanID = dtv.VanID and dtv.Statecode = ccv.StateCode
LEFT JOIN catalist_mdr.district_s ds
        on dtv.dwid = ds.dwid and dtv.StateCode = ds.state
WHERE DateCanvassed >= '2018-06-29'
 AND ContactTypeID in (2, 36)
 AND ccv.statecode = 'OH'
 GROUP BY ds.countyname
 ORDER BY ds.countyname ASC

-- grouping by DateCreated to see if certain days don't have full sync in VAN.
SELECT DateCreated::Date, COUNT(ccv.DateCreated)
FROM fof_vansync.contacts_contacts_vf as ccv
LEFT JOIN fof_vansync.dwid_to_van as dtv
       on ccv.VanID = dtv.VanID and dtv.Statecode = ccv.StateCode
LEFT JOIN catalist_mdr.district_s ds
        on dtv.dwid = ds.dwid and dtv.StateCode = ds.state
WHERE DateCanvassed >= '2018-06-29'
 AND ContactTypeID in (2, 36)
 AND ccv.statecode = 'OH'
GROUP BY DateCreated::Date
ORDER BY DateCreated ASC;

--pulling counts of total canvassed in a given week
SELECT COUNT(ccv.DateCanvassed)
FROM fof_vansync.contacts_contacts_vf as ccv
LEFT JOIN fof_vansync.dwid_to_van as dtv
       on ccv.VanID = dtv.VanID and dtv.Statecode = ccv.StateCode
LEFT JOIN catalist_mdr.district_s ds
        on dtv.dwid = ds.dwid and dtv.StateCode = ds.state
WHERE DateCanvassed >= '2018-06-29'
 AND ContactTypeID in (2, 36)
 AND ccv.statecode = 'OH'

-- Query 4 (Checking counts of all states since last week)
Select
    statecode
   ,Count(*)
From fof_vansync.contacts_contacts_vf
Where statecode in ('NV', 'VA', 'MI', 'FL', 'OH', 'WI', 'PA')
 and DateCanvassed >= '2018-07-06'
Group by statecode;