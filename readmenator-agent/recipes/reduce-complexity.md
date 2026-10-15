# Recipe: Reduce File Complexity

Target hotspot: `deploynator/_app.py`
(complexity 0.7, centrality 0.5)

1. Read dependents: `grep -n 'deploynator/_app.py' readmenator-agent/ARCHITECTURE*.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
