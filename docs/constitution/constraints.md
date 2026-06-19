<!--
last-updated: 2026-06-03
session-id: 2026-06-03-cold-start
author-agent: cowork
-->

# constraints.md — 구조적 금지 + 각 규칙이 어디서 강제되는가

> ⚠️ PLACEHOLDER — 아직 사람과 합의 전. 다음 세션에서 채운다.

## 쓰기 경계 (CLAUDE.md §4)
| 영역 | cowork | codex |
|---|---|---|
| constitution / plan / state / tasks/specs | 쓰기 | 읽기 |
| 실제 코드 / 데이터 | 읽기·검토 | 쓰기 |
| tasks/reports, log/sessions.md | 읽기·검증 | 쓰기(append) |
| log/decisions.md | 쓰기 | 읽기 |

## 강제 메커니즘 현황 (정직하게)
| 규칙 | 어디서 강제? | 상태 |
|---|---|---|
| 쓰기 경계 | (미정) git branch 보호 / read-only 마운트 / codex sandbox | ❌ 아직 없음 — 현재는 "부탁(soft)"일 뿐 |
| git 커밋은 사람 전용 (cowork는 디스크 쓰기까지만) | (미정) cowork 환경에서 git 실행 차단 | ⚠️ soft — 현재는 cowork의 자기규율로만. CLAUDE.md §4 + decisions.md(2026-06-03) 근거 |

> ⚠️ 현재 모든 경계는 문서 선언일 뿐 환경 메커니즘으로 강제되지 않음.
> 강제 메커니즘 설계는 향후 과제로 사람과 논의 필요.
