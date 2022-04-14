import torch
from transformers import ElectraForPreTraining, ElectraTokenizer, ElectraModel

model = ElectraModel.from_pretrained("monologg/koelectra-base-v2-discriminator")  # KoELECTRA-Base-v3
tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator")




class ElectraClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""

    def __init__(self, config):
        super().__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.out_proj = nn.Linear(config.hidden_size, config.num_labels)

    def forward(self, features, **kwargs):
        x = features[:, 0, :]  # take <s> token (equiv. to [CLS])
        x = self.dropout(x)
        x = self.dense(x)
        x = get_activation("gelu")(x)  # although BERT uses tanh here, it seems Electra authors used gelu here
        x = self.dropout(x)
        x = self.out_proj(x)
        return x


class ElectraForTokenClassification(ElectraPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels

        self.electra = ElectraModel(config)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        # Initialize weights and apply final processing
        self.post_init()

    @add_start_docstrings_to_model_forward(ELECTRA_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @add_code_sample_docstrings(
        processor_class=_TOKENIZER_FOR_DOC,
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=TokenClassifierOutput,
        config_class=_CONFIG_FOR_DOC,
    )
    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        token_type_ids=None,
        position_ids=None,
        head_mask=None,
        inputs_embeds=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        r"""
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        discriminator_hidden_states = self.electra(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        discriminator_sequence_output = discriminator_hidden_states[0]

        discriminator_sequence_output = self.dropout(discriminator_sequence_output)
        logits = self.classifier(discriminator_sequence_output)

        loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))

        if not return_dict:
            output = (logits,) + discriminator_hidden_states[1:]
            return ((loss,) + output) if loss is not None else output

        return TokenClassifierOutput(
            loss=loss,
            logits=logits,
            hidden_states=discriminator_hidden_states.hidden_states,
            attentions=discriminator_hidden_states.attentions,
        )









id2label={str(i): label for i, label in enumerate(self.label_lst)},
                                                        label2id={label: i for i, label in enumerate(self.label_lst)})



sentence = "나는 방금 밥을 먹었다."
fake_sentence = "나는 내일 밥을 먹었다."

fake_tokens = tokenizer.tokenize(fake_sentence)
print(fake_tokens, len(fake_tokens)) # ['나', '##는', '내일', '밥', '##을', '먹', '##었', '##다', '.'] 9
fake_inputs = tokenizer.encode(fake_sentence, return_tensors="pt") # tensor([[   2, 2236, 4034, 8258, 2739, 4292, 2654, 4480, 4176,   18,    3]])
# print(tokenizer.decode(0)) # 0 : PAD, # 1: UNK, # 2: CLS, #3: SEP, 
print(fake_inputs, len(fake_inputs))


discriminator_outputs = model(fake_inputs)
predictions = torch.round((torch.sign(discriminator_outputs[0]) + 1) / 2)

print(discriminator_outputs)
print(discriminator_outputs[0].size()) # 1, 11, 768 -> 9 + 2 ([cls] [sep] tokens을 붙인 상태임! 즉, 제일 첫 번째 index가 CLS인 것

hidden_states = discriminator_outputs[0]

# print(list(zip(fake_tokens, predictions.tolist()[1:-1])))

# concat 이후 
# loss만 잘 반환해 주면 됨 

class ElectraClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""

    def __init__(self, config):
        super().__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        classifier_dropout = (
            config.classifier_dropout if config.classifier_dropout is not None else config.hidden_dropout_prob
        )
        self.dropout = nn.Dropout(classifier_dropout)
        self.out_proj = nn.Linear(config.hidden_size, config.num_labels)

    def forward(self, features, **kwargs):
        x = features[:, 0, :]  # take <s> token (equiv. to [CLS])
        x = self.dropout(x)
        x = self.dense(x)
        x = get_activation("gelu")(x)  # although BERT uses tanh here, it seems Electra authors used gelu here
        x = self.dropout(x)
        x = self.out_proj(x)
        return x


class ElectraClassifier(nn.Module):
    
    def __init__(self):
        super(ElectraClassifier, self).__init__()
        
        # classifier 
        self.electra = ElectraModel()
        
        h1 = nn.Linear(hidden_states, 50)
        h2 = nn.Linear(50, 35)
        h3 = nn.Linear(35, 1)
        
        
        self.hidden = nn.Sequential(
            h1,
            nn.Tanh(),
            h2,
            nn.Tanh(),
            h3,
        )
        
        if use_cuda:
            self.hidden = self.hidden.cuda()
        
    def forward(self, x):
        o = self.hidden(x)
        return o.view(-1)

# 여기에 labels
model = newTokenizer(config)