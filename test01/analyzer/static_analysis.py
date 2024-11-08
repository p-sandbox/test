#정적 분석 구현
import hashlib

def perform_static_analysis(file):
    # 파일 해시 계산
    file_content = file.read()
    file_hash = hashlib.sha256(file_content).hexdigest()
    
    # 메타데이터 추출 등 추가 가능
    return {
        "file_hash": file_hash,
        "file_size": len(file_content)
    }
