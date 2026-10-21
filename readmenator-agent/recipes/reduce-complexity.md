# Recipe: Reduce File Complexity

Target hotspot: `deploynator/_config.py`
(complexity 0.1, centrality 1.0)

1. Read dependents: `grep -n 'deploynator/_config.py' readmenator-agent/ARCHITECTURE*.md`
2. Extract functions/classes into new files in the same subsystem
3. Update imports
4. Regenerate: `readmenator .`
