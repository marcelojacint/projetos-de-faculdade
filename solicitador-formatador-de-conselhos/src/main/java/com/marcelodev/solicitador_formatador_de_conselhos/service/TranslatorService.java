package com.marcelodev.solicitador_formatador_de_conselhos.service;

import org.springframework.stereotype.Service;

import com.google.cloud.translate.Translate;
import com.google.cloud.translate.TranslateOptions;
import com.google.cloud.translate.Translation;

@Service
public class TranslatorService {

	

	private Translate translate;

	public TranslatorService() {
		this.translate = TranslateOptions.getDefaultInstance().getService();
	}

	public String translateToPortuguese(String textToTranslate) {
		
		 Translate translate = TranslateOptions.newBuilder()
		            .setApiKey("AIzaSyDa2sI4_nbNAomkNaLw0BxFO5CG71iEi8U") // Substitua pela sua chave de API
		            .build()
		            .getService();
		
		Translation translation = translate.translate(textToTranslate, Translate.TranslateOption.sourceLanguage("en"),
				Translate.TranslateOption.targetLanguage("pt"));

		return translation.getTranslatedText();
	}

}
