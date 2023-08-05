//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseGeometryModel = require('../core/BaseGeometry.autogen.js').BaseGeometryModel;


class ConeGeometryModel extends BaseGeometryModel {

    defaults() {
        return _.extend(BaseGeometryModel.prototype.defaults.call(this), {

            radius: 20,
            height: 100,
            radialSegments: 8,
            heightSegments: 1,
            openEnded: false,
            thetaStart: 0,
            thetaLength: 6.283185307179586,
            type: "ConeGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.ConeGeometry(
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.convertFloatModelToThree(this.get('height'), 'height'),
            this.get('radialSegments'),
            this.get('heightSegments'),
            this.convertBoolModelToThree(this.get('openEnded'), 'openEnded'),
            this.convertFloatModelToThree(this.get('thetaStart'), 'thetaStart'),
            this.convertFloatModelToThree(this.get('thetaLength'), 'thetaLength')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['height'] = 'convertFloat';
        this.property_converters['radialSegments'] = null;
        this.property_converters['heightSegments'] = null;
        this.property_converters['openEnded'] = 'convertBool';
        this.property_converters['thetaStart'] = 'convertFloat';
        this.property_converters['thetaLength'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

ConeGeometryModel.model_name = 'ConeGeometryModel';
ConeGeometryModel.serializers = {
    ...BaseGeometryModel.serializers,
};

module.exports = {
    ConeGeometryModel: ConeGeometryModel,
};
