# Changelog

All notable changes to the Personality Test skill will be documented in this file.

## [2.0.0] - 2026-01-31

### Changed - MAJOR REDESIGN
- **Complete workflow overhaul**: Agent now self-scores in one interaction
- **Removed manual steps**: No longer requires copying responses or running external scripts
- **Embedded calculation logic**: Agent applies reverse-scoring and calculates averages automatically
- **Clearer instructions**: Step-by-step scoring guide embedded in SKILL.md
- **Better research citations**: Added nuance to claims and proper sourcing
- **Added disclaimer**: Clarified items are based on BFI framework, not official copyrighted inventory

### Added
- Self-scoring instructions in SKILL.md
- Detailed calculation steps (reverse-scoring, averaging, interpretation)
- Formatted output template for consistency
- Research foundation section with 2025-2026 citations
- SOCIAL_POSTS.md with ready-to-use marketing content
- CHANGELOG.md (this file)

### Improved
- README now emphasizes one-step workflow
- DEMO.md includes testing scenarios and troubleshooting
- Python script repositioned as optional verification tool (not required)
- Version bump to 2.0.0 reflecting breaking workflow changes

### Fixed
- Misleading claims about automation (v1.0 claimed automatic scoring but required manual steps)
- Research misapplication (clarified 85% accuracy context)
- Temperature enforcement (documented as best practice, not enforced)
- Integration workflow (now actually works in one step)

## [1.0.0] - 2026-01-31 (Deprecated)

### Added - Initial Release
- 44-item BFI-44 personality assessment
- Python scoring script with reverse-scoring logic
- Basic SKILL.md with test items
- README with installation instructions

### Issues (Fixed in v2.0.0)
- Required manual 3-step process (not "super easy")
- Workflow broken for autonomous execution
- External script dependency
- Misleading automation claims

---

## Migration Guide: v1.0.0 → v2.0.0

**If you're using v1.0.0:**

OLD workflow:
```bash
/personality-test
# Then manually copy comma-separated response
python3 score.py "1,2,3,..."
```

NEW workflow:
```bash
/personality-test
# That's it - results appear automatically
```

**The Python script (`score.py`) is still included** for manual verification, but it's now optional. The agent handles all scoring internally.

**No breaking changes to script API** - If you were using score.py programmatically, it still works the same way.

---

## Roadmap

### Planned for v2.1.0
- [ ] Multi-language support (Spanish, French, German)
- [ ] JSON output option for programmatic use
- [ ] Comparison mode (run multiple times, show consistency metrics)
- [ ] Visualization option (radar chart of Big Five scores)

### Planned for v3.0.0
- [ ] Additional inventories (IPIP-NEO-120, HEXACO, SD-3)
- [ ] Facet-level scoring (sub-traits within Big Five)
- [ ] Historical tracking (save and compare results over time)
- [ ] Team analysis (aggregate scores for multi-agent systems)

### Under Consideration
- [ ] API endpoint for remote testing
- [ ] Integration with popular agent frameworks
- [ ] Statistical validation suite
- [ ] Research toolkit (export data for analysis)

---

## Contributing

See GitHub issues for planned features and known bugs. Pull requests welcome!

For major changes, please open an issue first to discuss what you'd like to change.

## License

MIT License - See LICENSE file for details
