SELECT
 statecode
 ,COUNT(VAN_ccvf.ResultID) AS total_conversations
FROM fof_vansync.contacts_contacts_vf VAN_ccvf
LEFT JOIN fof_vansync.results VAN_r on VAN_ccvf.ResultID = VAN_r.ResultID
LEFT JOIN fof_vansync.contact_types VAN_ct on VAN_ccvf.ContactTypeID = VAN_ct.ContactTypeID
WHERE VAN_ccvf.DateCanvassed >= '2018-01-01'
 AND VAN_ccvf.ContactTypeID = 2 --walk contact type
 AND VAN_r.ResultID = 14 --find total conversations
GROUP BY statecode
