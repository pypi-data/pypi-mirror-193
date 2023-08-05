//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;

var RayModel = require('../math/Ray.autogen.js').RayModel;

class RaycasterModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            origin: [0,0,0],
            direction: [0,0,0],
            near: 0,
            far: 1000000,
            ray: null,
            linePrecision: 1,

        });
    }

    constructThreeObject() {

        var result = new THREE.Raycaster(
            this.convertVectorModelToThree(this.get('origin'), 'origin'),
            this.convertVectorModelToThree(this.get('direction'), 'direction'),
            this.convertFloatModelToThree(this.get('near'), 'near'),
            this.convertFloatModelToThree(this.get('far'), 'far')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('ray');


        this.property_converters['origin'] = 'convertVector';
        this.property_converters['direction'] = 'convertVector';
        this.property_converters['near'] = 'convertFloat';
        this.property_converters['far'] = 'convertFloat';
        this.property_converters['ray'] = 'convertThreeType';
        this.property_converters['linePrecision'] = 'convertFloat';

        this.property_assigners['origin'] = 'assignVector';
        this.property_assigners['direction'] = 'assignVector';

    }
}

RaycasterModel.model_name = 'RaycasterModel';
RaycasterModel.serializers = {
    ...ThreeModel.serializers,
    ray: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    RaycasterModel: RaycasterModel,
};
