from rest_framework import serializers

from camp_fin.models import Candidate, PAC, Transaction, LoanTransaction, Loan

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'

class PACSerializer(serializers.ModelSerializer):

    class Meta:
        model = PAC
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'

class LoanTransactionSerializer(serializers.ModelSerializer):
    loan = LoanSerializer(read_only=True)
    transaction_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = LoanTransaction
        fields = '__all__'

class EntityField(serializers.RelatedField):

    def to_representation(self, value):
        
        try:
            if value.entity.pac_set.all():
                serializer = PACSerializer(value.entity.pac_set.first())
            
            elif value.entity.candidate_set.all():
                serializer = CandidateSerializer(value.entity.candidate_set.first())

            return serializer.data
        except AttributeError:
            return value


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = serializers.StringRelatedField(read_only=True)
    full_name = serializers.StringRelatedField(read_only=True)
    transaction_subject = EntityField(read_only=True)

    class Meta:
        model = Transaction
        
        fields = (
            'id',
            'amount', 
            'received_date', 
            'date_added', 
            'check_number',
            'memo',
            'description',
            'transaction_type',
            'name_prefix',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'company_name',
            'full_name',
            'address',
            'city',
            'state',
            'zipcode',
            'full_address',
            'country',
            'occupation',
            'expenditure_for_certified_candidate',
            'transaction_subject'
        )

class TransactionSearchSerializer(TransactionSerializer):
    pac_slug = serializers.StringRelatedField(read_only=True)
    candidate_slug = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Transaction
        
        fields = (
            'id',
            'amount', 
            'received_date', 
            'date_added', 
            'check_number',
            'memo',
            'description',
            'transaction_type',
            'name_prefix',
            'first_name',
            'middle_name',
            'last_name',
            'suffix',
            'company_name',
            'full_name',
            'address',
            'city',
            'state',
            'zipcode',
            'full_address',
            'country',
            'occupation',
            'expenditure_for_certified_candidate',
            'transaction_subject',
            'pac_slug',
            'candidate_slug',
        )

class CandidateSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = (
            'id',
            'prefix',
            'first_name',
            'middle_name',
            'last_name',
            'full_name',
            'suffix',
            'business_phone',
            'home_phone',
            'date_added',
            'email',
            'date_updated',
            'deceased',
            'slug',
        )

class PACSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = PAC
        fields = (
            'id',
            'name',
            'acronym',
            'business_phone',
            'home_phone',
            'email',
            'date_added',
            'date_updated',
            'bank_name',
            'bank_phone',
            'fax_number',
            'initial_balance',
            'initial_balance_from_self',
            'initial_debt',
            'initial_debt_from_self',
            'slug',
        )

class TopMoneySerializer(serializers.Serializer):
    name_prefix = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    suffix = serializers.CharField()
    company_name = serializers.CharField()
    amount = serializers.CharField()
    last_date = serializers.DateTimeField()
