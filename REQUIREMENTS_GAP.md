# Assignment acceptance checklist

This checklist is intentionally conservative. A feature is not marked complete merely because a similarly named route or model exists. Mark each item complete only after implementation review and passing tests against PostgreSQL.

## Required acceptance checks

- [ ] Roles exactly cover Admin, Warehouse Manager, Fulfillment Agent, Customer.
- [ ] JWT register/login/refresh/logout/me/change-password; refresh rotation and revocation; inactive-user rejection.
- [ ] Product and warehouse lifecycle APIs; unique SKU; inactive products blocked from new orders.
- [ ] Inventory quantities separated by warehouse: available, reserved, damaged, reorder level.
- [ ] Immutable inventory ledger with all required transaction types and actor/reference metadata.
- [ ] Inventory adjustment and transfer use one transaction; transfer writes both TRANSFER_OUT and TRANSFER_IN.
- [ ] Multi-line order creation reserves stock atomically, uses stable price snapshots, and prevents overselling under concurrent PostgreSQL requests.
- [ ] Complete order state machine including Processing, Packed, Shipped, Delivered, Cancelled, Failed, Returned; all transitions recorded and invalid transitions rejected.
- [ ] Cancellation releases reservations and creates ledger, notification, and audit records atomically.
- [ ] Warehouse-scoped manager and fulfillment-agent authorization; assignment/reassignment rules and audit/notification.
- [ ] Returns Requested/Approved/Rejected/Received/Refunded with authorization, transition checks, and inventory updates.
- [ ] Server-side pagination, sorting, filtering; low-stock and out-of-stock APIs and threshold notifications.
- [ ] Notifications for all required events, read-one and read-all APIs, and reliable failure handling.
- [ ] Role-appropriate dashboard/reporting metrics.
- [ ] Immutable audit logs for required security and business events.
- [ ] Idempotency keys for order creation, payment confirmation, inventory adjustment, and transfer, including payload conflict behavior.
- [ ] Centralized domain error format and appropriate 400/401/403/404/409/422/500 responses.
- [ ] PostgreSQL constraints, indexes, foreign keys, Alembic migrations, ER diagram and database design explanation.
- [ ] Pytest positive and negative tests for auth, authorization, products, inventory, orders, returns, idempotency, and concurrency.
- [ ] Postman collection, architecture diagram, complete API examples, setup documentation, `.env.example`.

## Existing application gaps known from source review

The uploaded application is a useful starting point but currently has a narrower e-commerce workflow. The source includes authentication, products/categories, basic inventory/orders/payments/reviews/notifications/dashboard modules and an existing Alembic migration history. It does not yet demonstrate the full warehouse-level inventory ledger, complete assignment/returns workflows, full refresh-token lifecycle, idempotency implementation, or the required automated test coverage. Its existing Staff role is not equivalent to the two separate Warehouse Manager and Fulfillment Agent roles without explicit policy and resource-scope enforcement.

## Before production

- [ ] Fresh PostgreSQL volume migration succeeds from zero.
- [ ] Frontend production build and lint succeed.
- [ ] Backend unit/API tests pass.
- [ ] Integration tests pass against PostgreSQL (not SQLite substitutes for locking behavior).
- [ ] Concurrency test proves two requests cannot reserve the same final unit.
- [ ] Failure injection proves transfer/order/cancellation rollback is complete.
- [ ] Security review covers object-level authorization, token storage/revocation, CORS, upload validation, rate limiting, and secret handling.
- [ ] Backup restore, TLS, logging/monitoring, and deployment rollback have been rehearsed.
