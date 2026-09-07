# SQLite Projection

`schema.sql` is a dependency-free SQLite target for future querying. JSONL remains canonical during early research because it is append-friendly and easy to review. Before creating a database or importer, document migrations, conflict handling, and provenance retention in `database/migrations/` and the changelog.

Create a local projection only when needed:

```sh
sqlite3 venture-engine.db < schema.sql
```

Do not add untracked production data to SQLite until the import process is validated.
