SELECT co.id,
       COUNT(ord."inDelivery")
FROM "Couriers" AS co
INNER JOIN "Orders" AS ord ON co.id = ord."courierId"
GROUP BY co.id;