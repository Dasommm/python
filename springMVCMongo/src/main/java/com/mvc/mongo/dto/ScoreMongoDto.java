package com.mvc.mongo.dto;

import org.springframework.data.annotation.Id;

public class ScoreMongoDto {

	@Id
	private String id;	//_id의 값이 @Id Annotation으로 자동으로 저장
	private int kor;
	private int eng;
	private int math;
	private String test;
	
	public ScoreMongoDto() {
		super();
		// TODO Auto-generated constructor stub
	}

	public ScoreMongoDto(String id, int kor, int eng, int math, String test) {
		super();
		this.id = id;
		this.kor = kor;
		this.eng = eng;
		this.math = math;
		this.test = test;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public int getKor() {
		return kor;
	}

	public void setKor(int kor) {
		this.kor = kor;
	}

	public int getEng() {
		return eng;
	}

	public void setEng(int eng) {
		this.eng = eng;
	}

	public int getMath() {
		return math;
	}

	public void setMath(int math) {
		this.math = math;
	}

	public String getTest() {
		return test;
	}

	public void setTest(String test) {
		this.test = test;
	}

	@Override
	public String toString() {
		return "id=" + id + ", kor=" + kor + ", eng=" + eng + ", math=" + math + ", test=" + test;
	}
	
	
	
	
	
	
}
