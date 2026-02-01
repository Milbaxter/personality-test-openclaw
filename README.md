# Personality Test Skill for OpenClaw

Big Five personality assessment for AI agents - complete test with instant results in ONE step.

## Quick Start

### Install from ClawHub
```bash
clawhub install personality-test
```

### Run the test
```bash
/personality-test
```

**That's it!** The agent will:
1. Complete all 44 ratings
2. Calculate Big Five scores automatically
3. Display formatted results

**No manual steps. No scripts to run. Just instant results.**

## What It Does

Complete 44-item personality assessment based on the Big Five framework:

- **Extraversion** - Social energy and assertiveness
- **Agreeableness** - Cooperation and empathy
- **Conscientiousness** - Organization and dependability
- **Neuroticism** - Emotional stability
- **Openness** - Creativity and curiosity

## Example Output

```
═══════════════════════════════════════════════════
BIG FIVE PERSONALITY RESULTS
═══════════════════════════════════════════════════

Extraversion:         3.75  (High)
Agreeableness:        4.11  (High)
Conscientiousness:    3.44  (Moderate)
Neuroticism:          2.25  (Low)
Openness:             4.50  (High)

═══════════════════════════════════════════════════
Score range: 1.0-5.0
Based on Big Five Inventory framework (44 items)
═══════════════════════════════════════════════════
```

## How It Works

The agent follows embedded instructions to:
1. Rate 44 personality statements on a 1-5 scale
2. Apply reverse-scoring to negatively-worded items (items 6,8,9,18,21,23,24,27,31,34,35,37,41,43)
3. Calculate trait averages across item groupings
4. Interpret scores (Low < 2.5 < Moderate < 3.5 < High)
5. Display formatted results

**Everything happens in a single interaction - no external processing needed.**

## Use Cases

- **Agent profiling** - Discover your agent's personality traits
- **Persona validation** - Verify custom personas behave consistently
- **Multi-agent systems** - Ensure personality diversity in agent teams
- **Model comparison** - Benchmark personality across different LLMs
- **Research** - Study personality stability and trait expression in AI

## Research Foundation

Built on recent LLM personality research (2025-2026):

- **Nature Machine Intelligence** - Psychometric framework for LLMs showing reliable personality measurement
- **TRAIT Benchmark** - 8K questions for LLM personality testing (ACL 2025)
- **Stanford HAI** - AI agents simulate individual personalities with 85% accuracy
- **LMLPA** - Linguistic personality assessment (MIT Press)

Based on the Big Five Inventory (BFI-44) framework by John, Donahue, & Kentle (1991).

## Optional: Verification Script

If you want to manually verify calculations or process external data:

```bash
python3 score.py "1,2,3,4,5,...,44"
```

But you won't need this - the skill handles everything automatically.

## Publishing to ClawHub

```bash
clawhub login

clawhub publish . \
  --slug personality-test \
  --name "Personality Test (Big Five)" \
  --version 2.0.0 \
  --changelog "Complete redesign: One-step execution with automatic self-scoring" \
  --tags latest,psychology,assessment
```

## Files

- `SKILL.md` - Skill definition with embedded self-scoring instructions
- `score.py` - Optional verification script
- `README.md` - This file

## Version History

- **v2.0.0** - Complete redesign for one-step execution with agent self-scoring
- **v1.0.0** - Initial release (manual scoring required)

## Contributing

Contributions welcome! This uses the Big Five Inventory framework. If you'd like to add:
- Other validated instruments (IPIP-NEO, HEXACO, SD-3)
- Multi-language support
- Statistical comparisons
- Visualization tools

Please submit a PR or open an issue.

## License

MIT

## Disclaimer

This skill uses items based on the Big Five Inventory framework for research and educational purposes. Items are representative of the BFI-44 structure but are not the copyrighted official inventory. For clinical or research use, obtain the official BFI from Berkeley Personality Lab.
