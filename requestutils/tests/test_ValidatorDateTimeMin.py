import nose.tools as nt
import validators
import datetime


class TestValidatorDateTimeMin(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_description(self):
        validator = validators.ValidatorDateTimeMin('2007-03-04T21:08:12.000')
        nt.eq_(validator.description, 'Validate parameter if ISO8601 Date time later than <2007-03-04T21:08:12.000>')

    def test_create_pass(self):
        '''
        should pass when creating validator from valid datetime string
        '''
        nt.ok_(validators.ValidatorDateTimeMin('2007-03-04T21:08:12.000'))

    def test_create_fail(self):
        '''
        should fail when created with invalid parameter
        '''
        nt.assert_raises(validators.ValidatorError, validators.ValidatorDateTimeMin, '2007-03i-04T21:08:12.000')

    def test_passes_valid(self):
        '''
        should pass when trying to validate a valid date that is after mindate
        should return a valid datetime
        '''
        validator = validators.ValidatorDateTimeMin('2007-03-04T21:08:12.000')
        dt = validator.check('2007-04-04T21:08:12.000')
        assert isinstance(dt, datetime.datetime)

    def test_fails_on_earlier_date(self):
        '''
        Should fail with propper message when validating datetime that is before mindt
        '''
        validator = validators.ValidatorDateTimeMin('2007-03-04T21:08:12.000')
        nt.assert_raises(validators.ValidatorError, validator.check, '2007-02-04T21:08:12.000')

        try:
            validator.check('2007-02-04T21:08:12.000')
        except validators.ValidatorError as e:
            nt.eq_(e.message, 'Supplied parameter <2007-02-04T21:08:12.000> is not a valid ISO8601 Date time after <2007-03-04T21:08:12.000>')
