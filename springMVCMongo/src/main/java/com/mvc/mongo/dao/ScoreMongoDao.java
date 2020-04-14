package com.mvc.mongo.dao;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Repository;

import com.mvc.mongo.dto.ScoreMongoDto;

@Repository
public class ScoreMongoDao {

	@Autowired
	private MongoTemplate mongoTemplate;
	
	public List<ScoreMongoDto> findAll(){
		
		List<ScoreMongoDto> list = mongoTemplate.findAll(ScoreMongoDto.class,"score");
		
		return list;
	}
	
}
