<!--
last-updated: <YYYY-MM-DD>
session-id: <codex 세션 식별자>
author-agent: codex
-->

# REPORT-<번호> — <짝 spec과 같은 제목>

> codex가 SPEC-<번호> 수행 후 작성. cowork가 이 report를 spec과 **대조 검증**한다.
> report 없는 변경은 "검증 불가"로 간주되어 받아들여지지 않는다.

| 항목 | 값 |
|---|---|
| report-id | REPORT-<번호> |
| 짝 spec | SPEC-<번호> |
| 수행일 | <YYYY-MM-DD> |
| 수행자 | codex |
| 상태 | <완료 / 부분완료 / 막힘> |

## 1. 무엇을 했나 (What was done)
<실제로 수행한 것. spec의 목표 대비.>

## 2. 어떻게 (How — 메커니즘·구조)
<핵심 접근/구조/선택. cowork가 결과를 신뢰하려면 '어떻게'를 알아야 한다.>

## 3. 완료조건 자가체크 (spec §5 대조)
<spec의 완료조건을 그대로 옮겨 각 항목에 증거를 단다.>
- [x] <조건> — 증거: `outputs/...` / 명령 / 로그
- [ ] <미충족 조건> — 사유:

## 4. 못 한 것 · 막힌 것 (Blocked / Incomplete) ⚠️ 숨기지 말 것
<실패·미완·불확실을 정직하게. 없으면 "없음".>

## 5. 추적 흔적 (Traces — 사람이 따라갈 수 있게)
<재현 명령, 산출 파일 경로, 커밋 해시, 로그 위치 등.>
- 재현: `<명령>`
- 산출물: `outputs/...`
- 커밋: `<hash>`

## 6. cowork에게 넘기는 질문 / 다음 제안 (있으면)
<후속 spec이 필요한 부분, 사람 판단이 필요한 갈림길 등.>

---
> ✅ 이 report 작성 후 codex는 `docs/log/sessions.md` 에 한 줄 append 한다.
