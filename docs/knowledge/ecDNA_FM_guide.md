# ecDNA × Foundation Models 프로젝트

---

## 프로젝트가 무엇인가

### 한 줄 요약

**Foundation model을 이용해서 암세포의 ecDNA를 single-cell 수준에서 characterize하고, sequence와 cell state의 관계를 밝힌다.**

### 조금 더 풀어쓰면

암세포 안에는 **ecDNA (extrachromosomal DNA)** 라는 구조가 있습니다. 정상 chromosome 밖에 떠다니는 원형의 DNA 조각인데, MYC, EGFR, MYCN 같은 oncogene을 수십~수백 copy 가지고 있어서 암을 강력하게 drive 하는 것으로 최근에 알려지고 있습니다. 일반적인 amplification (BFB cycle, complex non-cyclic amplification) 과 다른 점은 *centromere가 없어서 mitosis 때 random하게 daughter cell에 분배된다는 것*. 그래서 같은 tumor 안에서도 cell마다 ecDNA copy 수가 천차만별이고, 이게 drug resistance나 tumor evolution에 핵심 역할을 합니다.

최근 몇 년 사이 **foundation model (FM)** 이 생물학에 빠르게 들어오고 있습니다. DNA 서열을 학습한 DNA FM (Evo2, Nucleotide Transformer 등), single-cell expression을 학습한 scFM (Geneformer, scGPT 등) 이 대표적입니다.

이 프로젝트는 **두 흐름을 결합** 합니다:

1. ecDNA-positive cell line의 scRNA-seq에 scFM을 적용해서 *ecDNA-carrying cell* 의 transcriptional state를 잡아낼 수 있나
2. 그 cell들이 carry하는 ecDNA의 *junction sequence* 를 DNA FM으로 분석해서 sequence-level signature가 있나
3. 두 layer를 연결해서 ecDNA biology를 multi-scale로 이해

### 왜 흥미로운가

- **Cell-level question**: ecDNA carrier cell을 transcriptome만으로 구분할 수 있다면, 비싼 wet-lab ecDNA detection 없이도 ecDNA biology를 연구할 수 있습니다.
- **Sequence-level question**: ecDNA의 junction이 BFB나 다른 amplification과 sequence level에서 다른가? 이건 ecDNA biology의 long-standing 질문이고, 답이 yes든 no든 모두 흥미로운 결과입니다.
- **Method-level question**: scFM과 DNA FM이 ecDNA 같은 cancer-specific structure를 학습했는가, 아니면 일반적인 pattern만 학습했는가?

연구는 항상 *답이 yes인지 no인지 모르는 상태* 에서 시작합니다. 결과가 예상과 달라도 잘 설계되어 진행된다면 의미있는 finding입니다.

---

## 큰 그림


| Phase | 핵심 작업 | 
|---|---|
| A | Onboarding (background + dataset 매핑 + 도구 학습) |
| B | Frozen scFM × ecDNA carrier detection |
| C | Cross cell-line + dosage 확장 |
| D | DNA FM × junction sequence 분석 |
| E | (Optional) Structure layer (Akita/Orca) |


각 phase의 *결과* 가 다음 phase의 방향을 결정합니다. 미리 모든 것을 정해두지 않고, 결과에 따라 진행하면서 조정합니다.

---

## Phase A — Onboarding

**목표**: 프로젝트에 필요한 배경 지식과 도구를 익히고, 사용할 dataset list를 확정한다.

### A.1 — 필수 reading

**다음 paper들을 먼저 읽기**

ecDNA biology (이게 우리가 푸는 *문제* 의 영역) - 예시이고, 관련된 다른 논문들을 봐도 됩니다.:
1. **Wu et al. 2019, *Nature*** — Circular ecDNA promotes accessible chromatin and high oncogene expression
2. **Hung et al. 2021, *Nature*** — ecDNA hubs drive cooperative intermolecular oncogene expression
3. **Lange et al. 2022, *Nat Genet*** — Evolutionary dynamics of ecDNA in human cancers (이게 single-cell 측면을 다룹니다)

scFM (이게 우리가 쓸 *도구* 의 영역):
4. **Theodoris et al. 2023, *Nature*** — Geneformer
5. **Cui et al. 2024, *Nat Methods*** — scGPT

**더 깊이 읽기**

- Wang et al. 2024, *Nat Commun* — HAPI (3D genomic analysis of enhancer hijacking on ecDNA)
- Bafna & Mischel 2022 — ecDNA review
- Geneformer V2 cancer-tuned update (2024.09)
- scFM critique/benchmark 논문들 (예: scEval, Boiarsky 2024 등)


### A.2 — 도구 학습

**scanpy tutorial**
- 공식 tutorial (https://scanpy.readthedocs.io) 의 PBMC3K 예제를 처음부터 끝까지 따라가기
- QC, normalization, HVG selection, PCA, UMAP, Leiden clustering 전체 flow

**scFM API 학습**
- Geneformer (HuggingFace): pretrained model 불러오기, embedding 추출
- scGPT (공식 GitHub): pretrained checkpoint 다운로드, embedding 추출
- 작은 test dataset (PBMC3K 같은) 에서 embedding을 뽑아서 UMAP까지 그려보기

**Ground truth pipeline 학습**
- inferCNV 또는 CopyKAT tutorial 완주
- scRNA-seq에서 cell별 copy number를 *추정* 하는 도구. 우리 프로젝트에서 ecDNA carrier vs non-carrier를 정의하는 ground truth로 사용합니다.


### A.3 — Dataset 매핑 (핵심 deliverable)

우리 프로젝트는 *ecDNA-positive cell line의 scRNA-seq* 가 필요합니다. 다음 작업:

1. **AmpliconRepository.org에 academic email로 registration**
2. **CCLE 329 cell line의 AmpliconArchitect output 다운로드**, ecDNA로 classified된 line 추출
3. **scRNA-seq이 있는 cell line cross-reference**:
   - Kinker et al. 2020 atlas (198개 cell line scRNA-seq) 에서 ecDNA-positive line 찾기
   - 개별 published ecDNA-positive cell line scRNA-seq GEO accession 정리:
     - Hung 2021 COLO320DM
     - Mischel lab GBM39, HK301
     - Henssen lab neuroblastoma CHP-212, IMR-5/75
     - 기타 search로 찾기
4. **최종 target list 작성**: 우선 사용할 3-5개 cell line + 추가 후보 5-10개

이 dataset mapping이 Phase A의 가장 중요한 deliverable입니다. 


---

## Phase B — Frozen scFM × ecDNA carrier detection (메인 작업)

**목표**: scFM이 *zero-shot* (별도 학습 없이) 으로 ecDNA carrier cell을 transcriptome만 보고 구분할 수 있는지 평가한다.

### 왜 frozen-first인가

Foundation model을 사용하는 두 가지 방식이 있습니다:
- **Frozen**: pretrained model의 parameter를 그대로 두고 embedding만 추출
- **Fine-tuning**: model을 우리 task에 맞춰 추가 학습

우리는 frozen으로 먼저 갑니다. 이유:
1. *Pretraining만으로 ecDNA를 학습했는지* 가 가장 흥미로운 질문
2. Compute/시간 부담이 훨씬 작음
3. Reproducibility 좋음
4. 결과가 충분히 좋으면 fine-tuning까지 안 가도 됨

Fine-tuning은 frozen이 부족할 때만 conditional하게 추가합니다.

### B.1 — scRNA-seq preprocessing

- 3-5개 ecDNA-positive cell line의 scRNA-seq 합쳐서 preprocessing
- QC: doublet removal (Scrublet), mitochondrial content filter
- Normalization (standard scanpy workflow)
- Cell line 간 batch effect 평가 — quantitative (kBET, LISI 등) + visual (UMAP)

### B.2 — Unsupervised frozen embedding 분석

세 가지 scFM을 평가:
- Geneformer base
- Geneformer cancer-tuned
- scGPT

각 scFM에서:
- Zero-shot embedding 추출
- UMAP + Leiden clustering
- inferCNV로 cell별 ecDNA copy number proxy 계산 → ground truth carrier label

**핵심 질문**: Clustering이 carrier subpopulation을 *자연스럽게* 분리하나?

### B.3 — Baseline 비교

scFM이 진짜 도움이 되는지 확인하려면 baseline과 비교해야 합니다:
- Standard pipeline (HVG + PCA + Leiden)
- scVI embedding

평가 지표:
- Adjusted Rand Index (ARI) — clustering vs ground truth
- Silhouette score
- Carrier cluster purity

### B.4 — Linear probing (supervised frozen)

Unsupervised clustering이 잘 안 잡아도, *embedding 안에 information이 있을 수 있습니다*. 이걸 확인하는 게 linear probing:

- Frozen embedding 위에 logistic regression / 작은 MLP
- Carrier vs non-carrier binary classification
- 두 가지 train/test split 둘 다 평가:
  - **Cell line 단위 split** (strict): hold-out cell line의 carrier를 예측할 수 있나
  - **Cell 단위 split**: 같은 cell line 내 carrier 예측

### B.5 — Layer-wise probing

이건 lab의 BERTology framework을 직접 적용하는 부분입니다:
- scGPT, Geneformer 각 layer별 embedding 추출
- 각 layer에서 linear probing 성능 측정
- "어느 layer가 ecDNA-relevant signal에 강한가" 답

### Phase B 끝 미팅에서 결정할 것

Phase B 결과에 따라 Phase C 방향이 결정됩니다. 결과를 정리해서 가져오면 같이 판단합니다.

---

